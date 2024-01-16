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
        self.p.Add(key = key.v)  # Documentation says Key, but it's key

    def clear(self) -> None:
        self.p.Clear()

    def get_count(self) -> int:
        count = ctypes.c_ulong()
        self.p.GetCount(pcElems = pointer(count))  # Not [out]
        return count.value

    def get_at(self, index: int) -> PropertyKey:
        key = PropertyKey.null()
        self.p.GetAt(dwIndex = index, pKey = pointer(key.v))
        return key

    def remove_at(self, index: int) -> None:
        self.p.RemoveAt(dwIndex = index)
