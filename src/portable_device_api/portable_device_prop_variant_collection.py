import ctypes
from ctypes import pointer
from typing import Any

from portable_device_api import PropVariant
from portable_device_api._api import portable_device_api, portable_device_types
from portable_device_api._util import ComWrapper


# https://learn.microsoft.com/en-us/windows/win32/wpd_sdk/iportabledevicepropvariantcollection
class PortableDevicePropVariantCollection(ComWrapper):
    # Class is only defined in portable_device_types, but the API functions are
    # in portable_device_api, so we need the interface from there.
    _type_ = portable_device_types.PortableDevicePropVariantCollection
    _interface_ = portable_device_api.IPortableDevicePropVariantCollection

    def add(self, value: PropVariant) -> None:
        value_pointer = pointer(value.v)
        self.p.Add(pValue = value_pointer)  # [in] POINTER(tag_inner_PROPVARIANT) pValue

    def get_count(self) -> int:
        count = ctypes.c_ulong()
        self.p.GetCount(pcElems = pointer(count))  # [in] POINTER(c_ulong) pcElems
        return count.value

    def get_at(self, index: int) -> Any:
        value = PropVariant.create()
        self.p.GetAt(
            dwIndex = index,            # [in] c_ulong dwIndex
            pValue = pointer(value.v))  # [in] POINTER(tag_inner_PROPVARIANT) pValue
        return value
