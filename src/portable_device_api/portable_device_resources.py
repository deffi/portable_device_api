import ctypes

import portable_device_api.definitions as defs
from portable_device_api import PortableDeviceDataStream
from portable_device_api._api import portable_device_api
from portable_device_api._util import ComWrapper


# https://learn.microsoft.com/en-us/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledeviceresources
class PortableDeviceResources(ComWrapper):
    def get_stream(self, object_id: str) -> tuple[PortableDeviceDataStream, int]:
        """Yields stream, optimal buffer size"""

        # [in, out] POINTER(c_ulong) pdwOptimalBufferSize
        # [out] POINTER(POINTER(IStream)) ppStream
        optimal_buffer_size, stream = self.p.GetStream(
            pszObjectID = object_id,            # [in] WSTRING pszObjectID
            key = defs.WPD_RESOURCE_DEFAULT.v,  # [in] POINTER(_tagpropertykey) key
            dwMode = ctypes.c_uint(0))          # [in] c_ulong dwMode

        # Seems like this is an IPortableDeviceDataStream
        stream = stream.QueryInterface(portable_device_api.IPortableDeviceDataStream)
        return PortableDeviceDataStream(stream), optimal_buffer_size
