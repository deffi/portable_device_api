from contextlib import contextmanager


# For now, it seems like it is less confusing to just do this manually (we have
# to pass in two functions to use this), and we weren't using it all too often.
# We might want to re-enable this, but then we should consider (a) not using
# lambdas, and (b) inferring the size type and the value type from type
# annotations.
#
# def two_step_read(function, size_type, value_type, value_initializer):
#     """Implements a common COM API pattern for reading data (e.g., strings) of
#     variable size:
#       * To determine the size, a function is called with a null pointer and a
#         pointer to the size, which is updated by the function.
#       * To retrieve the data, the function is called again with a pointer to a
#         buffer (of the appropriate size) and, again, a pointer to the size.
#
#     Specifically:
#       * `function` will be called with a pointer to the buffer and a pointer to
#         the size. If the target function has additional parameters or a
#         different order, supply a wrapper.
#       * `size_type` is the type for the size (not a pointer to the size; e.g.,
#         ctypes.c_ulong).
#       * `value_type` is the type of one single value element; the number of
#         elements is given by the size.
#       * `value_initializer` will be called with the size (as `size_type`) and is
#         expected to return a pointer to a buffer of the appropriate size. The
#         value is cast to pointer-of-`value_type` for the call to `function`.
#
#     Example from PortableDeviceManager:
#         return two_step_read(
#             lambda pv, ps: self.p.GetDeviceDescription(
#                 pszPnPDeviceID = device_id,
#                 pDeviceDescription = pv,
#                 pcchDeviceDescription = ps),
#             c_ulong,
#             c_ushort, lambda s: create_unicode_buffer(s.value)).value
#     """
#     # Determine the length
#     size = size_type(0)
#     function(POINTER(value_type)(), pointer(size))
#
#     # Get the description
#     value_pointer = value_initializer(size)
#     function(cast(value_pointer, POINTER(value_type)), pointer(size))
#
#     return value_pointer


@contextmanager
def replace_methodspec(interface_class: type, method_name: str, mapping) -> None:  # TODO type annotation for mapping
    # As of comtypes 1.3.0, _ComMemberSpec is a NamedTuple, and therefore, we
    # have to replace the methodspec rather than modifying it in place.

    # noinspection PyProtectedMember
    for index, methodspec in enumerate(interface_class._methods_):
        if methodspec.name == method_name:
            methodspec = mapping(methodspec)
            interface_class._methods_[index] = methodspec

    # Otherwise, _cominterface_meta._make_methods (called via __setattr__) will refuse to replace it
    delattr(interface_class, method_name)
    # noinspection PyProtectedMember
    interface_class._methods_ = interface_class._methods_


def change_pflags(paramflags: tuple[tuple[int, str], ...], argname: str, pflags: int) -> tuple[tuple[int, str], ...]:
    """paramflags and return value are a sequence of (pflags, argname)

    Cf. comtypes._memberspec._resolve_argspec
    """

    def map_paramflag(paramflag: tuple[int, str]):
        if paramflag[1] == argname:
            return pflags, argname
        else:
            return paramflag

    return tuple(map(map_paramflag, paramflags))


def replace_methodspec_change_pflags(interface_class: type, method_name: str, argname: str, pflags: int):
    def mapping(methodspec):
        return methodspec._replace(paramflags = change_pflags(methodspec.paramflags, argname, pflags))

    replace_methodspec(interface_class, method_name, mapping)
