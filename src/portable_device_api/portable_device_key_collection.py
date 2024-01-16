import ctypes
from ctypes import pointer

from portable_device_api import PropertyKey
from portable_device_api._api import portable_device_api, portable_device_types
from portable_device_api._util import ComWrapper


# https://learn.microsoft.com/en-us/windows/win32/wpd_sdk/iportabledevicekeycollection
class PortableDeviceKeyCollection(ComWrapper):
    # Class is only defined in portable_device_types, but the API functions are
    # in portable_device_api, so we need the interface from there.
    _type_ = portable_device_types.PortableDeviceKeyCollection
    _interface_ = portable_device_api.IPortableDeviceKeyCollection

    def add(self, key: PropertyKey) -> None:
        # Documentation says Key, but it's key
        self.p.Add(key = key.v)  # [in] POINTER(_tagpropertykey) key

    def clear(self) -> None:
        self.p.Clear()

    def get_count(self) -> int:
        count = ctypes.c_ulong()
        self.p.GetCount(pcElems = pointer(count))  # [in] POINTER(c_ulong) pcElems
        return count.value

    def get_at(self, index: int) -> PropertyKey:
        key = PropertyKey.null()
        self.p.GetAt(
            dwIndex = index,        # [in] c_ulong dwIndex
            pKey = pointer(key.v))  # [in] POINTER(_tagpropertykey) pKey
        return key

    def remove_at(self, index: int) -> None:
        self.p.RemoveAt(dwIndex = index)  # [in] c_ulong dwIndex
