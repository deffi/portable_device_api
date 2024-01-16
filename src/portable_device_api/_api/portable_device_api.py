from ctypes import POINTER as _POINTER

from comtypes import COMMETHOD as _COMMETHOD, HRESULT as _HRESULT, GUID as _GUID
from comtypes.client import GetModule as _GetModule

import portable_device_api._util.comtypes as _comtypes_utils

_module = _GetModule("portabledeviceapi.dll")

# Since we don't get IDE autocompletion anyway, we might as well import the
# names we use explicitly, so we don't ge warnings about unresolved references.
# Alternative:
#     globals().update(_module.__dict__)

PortableDevice = _module.PortableDevice
IPortableDeviceValues = _module.IPortableDeviceValues
IPortableDevicePropVariantCollection = _module.IPortableDevicePropVariantCollection
PortableDeviceManager = _module.PortableDeviceManager
IPortableDeviceKeyCollection = _module.IPortableDeviceKeyCollection
IPortableDeviceValuesCollection = _module.IPortableDeviceValuesCollection
# noinspection PyProtectedMember
tagpropertykey = _module._tagpropertykey
tag_inner_PROPVARIANT = _module.tag_inner_PROPVARIANT
IStream = _module.IStream
WSTRING = _module.WSTRING


# We're modifying the method specs for two interfaces here. Both of them are
# generated with a parameter as [out], where we need to pass a pointer to a
# buffer (that we allocate) into the method, which only seems possible with [in,
# out].
#
# In the PortableDevices project[1], this is solved by manually modifying the
# generated Python file, _1F001332_1A57_4934_BE31_AFFC99F4EE0A_0_1_0.py, and
# replacing `['out']` with `['in', 'out']`. Note that they modify a total of 5
# parameters in 4 methods; for some of them, we can use the [out] parameter by
# using the return value (and passing all arguments as keyword arguments).
#
# It is currently unclear what's going wrong here; this might be based on a
# wrong understanding of COM or comtypes. If you know more, please contact the
# maintainer of this library or open an issue.
#
# [1] https://github.com/KasparNagu/PortableDevices
# [2] https://learn.microsoft.com/en-us/windows/win32/api/portabledeviceapi/nf-portabledeviceapi-ienumportabledeviceobjectids-next
# [3] https://learn.microsoft.com/de-de/dotnet/api/microsoft.sqlserver.dts.runtime.wrapper.isequentialstream.remoteread?view=sqlserver-2019

# This might be generated incorrectly, or the IDL might be incorrect: pObjIDs is
# generated with ['out'], but the documentation[2] says [in, out].
#
# Used in portable_device_api.enum_portable_device_object_ids.
with _comtypes_utils.modify_methodspec(_module.IEnumPortableDeviceObjectIDs, "Next") as method:
    method.paramflags = _comtypes_utils.change_pflags(method.paramflags, "pObjIDs", 3)  # 3: [in, out]

# The documentation situation isn't quite as clear here, as the only mention of
# ISequentialStream.RemoteRead I could find is in the documentation for
# Microsoft.SqlServer[3], and there it says [out]. The signature given there is
# in C#, so this might not be useful here.
#
# See portable_device_api.portable_device_data_stream.
with _comtypes_utils.modify_methodspec(_module.ISequentialStream, "RemoteRead") as method:
    method.paramflags = _comtypes_utils.change_pflags(method.paramflags, "pv", 3)  # 3: [in, out]


# The GUID and methods of the IPortableDeviceDataStream interface are from
# PortableDeviceApi.h.

class IPortableDeviceDataStream(IStream):
    _case_insensitive_ = True
    _iid_ = _GUID('{88e04db3-1012-4d64-9996-f703a950d3f4}')
    _idlflags_ = []

    _methods_ = [
        _COMMETHOD(
            [],
            _HRESULT,
            'GetObjectID',
            (['in', 'out'], _POINTER(WSTRING), 'ppszObjectID')

        ),
        _COMMETHOD([], _HRESULT, 'Cancel'),
    ]


# The union field of tag_inner_PROPVARIANT that contains the actual data is
# generated with the name __MIDL___MIDL_itf_PortableDeviceApi_0001_0000_0001,
# which is not only unwieldy but also private (insofar as "private" is a thing
# in Python). We cannot change tag_inner_PROPVARIANT._fields_ after it has been
# set (ctypes.Structure) does not allow that, so we add a property called
# `union` that accesses the field.

@property
def prop_variant_union(self):
    return self.__MIDL____MIDL_itf_PortableDeviceApi_0001_00000001


tag_inner_PROPVARIANT.union = prop_variant_union
