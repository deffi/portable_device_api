import ctypes
from ctypes import POINTER

from portable_device_api._util import ComWrapper


# https://learn.microsoft.com/en-us/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-ienumportabledeviceobjectids
class EnumPortableDeviceObjectIds(ComWrapper):
    def next(self, objects: int) -> list[str]:
        # noinspection PyTypeChecker,PyCallingNonCallable
        object_ids = (ctypes.c_wchar_p * objects)()

        # Patched, see portable_device_api._api.portable_device_api
        _, fetched_count = self.p.Next(
            cObjects = ctypes.c_ulong(objects),
            pObjIDs = ctypes.cast(object_ids, POINTER(ctypes.c_wchar_p)))

        return [object_ids[i] for i in range(fetched_count)]
