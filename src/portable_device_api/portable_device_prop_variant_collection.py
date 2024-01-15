import ctypes
from ctypes import POINTER, pointer, cast

from portable_device_api import PropVariant
from portable_device_api._api import portable_device_api, portable_device_types
from portable_device_api._util import ComWrapper


# https://learn.microsoft.com/en-us/windows/win32/wpd_sdk/iportabledevicepropvariantcollection
class PortableDevicePropVariantCollection(ComWrapper):
    # Class is only defined in portable_device_types, but the API functions are
    # in portable_device_api, so we need the interface from there.
    _type_ = portable_device_types.PortableDevicePropVariantCollection
    _interface_ = portable_device_api.IPortableDevicePropVariantCollection

    def add(self, value: PropVariant):
        value_pointer = pointer(value.v)
        self.p.Add(pValue = value_pointer)

    def get_count(self) -> int:
        count = ctypes.c_ulong()
        self.p.GetCount(pcElems = pointer(count))  # Not [out]
        return count.value

    def get_at(self, index: int):
        value = PropVariant.create()
        self.p.GetAt(
            dwIndex = index,
            pValue = pointer(value.v))
        return value
