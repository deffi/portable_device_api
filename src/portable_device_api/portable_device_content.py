import ctypes
from ctypes import c_ulong

from portable_device_api import PortableDevicePropVariantCollection, PortableDeviceValues
from portable_device_api import (PortableDeviceProperties, PortableDeviceResources, EnumPortableDeviceObjectIds,
                     PortableDeviceDataStream)
from portable_device_api._api import portable_device_api
from portable_device_api._util import ComWrapper
from portable_device_api._util.ctypes import null_pointer


# https://learn.microsoft.com/en-us/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledevicecontent
class PortableDeviceContent(ComWrapper):
    def enum_objects(self, parent_object_id: str) -> EnumPortableDeviceObjectIds:
        return EnumPortableDeviceObjectIds(self.p.EnumObjects(
            ctypes.c_ulong(0),
            parent_object_id,
            null_pointer(portable_device_api.IPortableDeviceValues)))

    def properties(self):
        return PortableDeviceProperties(self.p.Properties())

    def create_object_with_properties_and_data(self, values: PortableDeviceValues)\
            -> tuple[PortableDeviceDataStream, int]:
        """Yields stream, optimal buffer size"""

        data, optimal_write_buffer_size, _ = self.p.CreateObjectWithPropertiesAndData(pValues = values.p)

        # "After calling Commit to create the object, call QueryInterface on
        # ppData for IPortableDeviceDataStream, and then call
        # IPortableDeviceDataStream::GetObjectID to get the ID of the newly
        # created object."
        # But it seems that we can QueryInterface it right away (we just can't
        # call GetObjectID until after commit).
        # https://learn.microsoft.com/en-us/windows/win32/api/portabledeviceapi/nf-portabledeviceapi-iportabledevicecontent-createobjectwithpropertiesanddata
        data = data.QueryInterface(portable_device_api.IPortableDeviceDataStream)
        return PortableDeviceDataStream(data), optimal_write_buffer_size

    def create_object_with_properties_only(self, values: PortableDeviceValues) -> str:
        return self.p.CreateObjectWithPropertiesOnly(pValues = values.p)

    def transfer(self) -> PortableDeviceResources:
        return PortableDeviceResources(self.p.Transfer())

    def delete(self, options: int, object_ids: PortableDevicePropVariantCollection)\
            -> PortableDevicePropVariantCollection:
        options = c_ulong(options)

        result = self.p.Delete(
            dwOptions = options,
            pObjectIDs = object_ids.p)
        return PortableDevicePropVariantCollection(result)
