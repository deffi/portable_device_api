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
        # [out] POINTER(POINTER(IEnumPortableDeviceObjectIDs)) ppenum
        return EnumPortableDeviceObjectIds(self.p.EnumObjects(
            dwFlags = ctypes.c_ulong(0),                                         # [in] c_ulong dwFlags
            pszParentObjectID = parent_object_id,                                # [in] WSTRING pszParentObjectID
            pFilter = null_pointer(portable_device_api.IPortableDeviceValues)))  # [in] POINTER(IPortableDeviceValues) pFilter

    def properties(self):
        # [out] POINTER(POINTER(IPortableDeviceProperties)) ppProperties
        return PortableDeviceProperties(self.p.Properties())

    def create_object_with_properties_and_data(self, values: PortableDeviceValues)\
            -> tuple[PortableDeviceDataStream, int]:
        """Yields stream, optimal buffer size"""
        # [out] POINTER(POINTER(IStream)) ppData
        # [in, out] POINTER(c_ulong) pdwOptimalWriteBufferSize
        # [in, out] POINTER(WSTRING) ppszCookie
        data, optimal_write_buffer_size, _ = self.p.CreateObjectWithPropertiesAndData(
            pValues = values.p)  # [in] POINTER(IPortableDeviceValues) pValues

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
        # [in, out] POINTER(WSTRING) ppszObjectID
        return self.p.CreateObjectWithPropertiesOnly(pValues = values.p)  # [in] POINTER(IPortableDeviceValues) pValues

    def transfer(self) -> PortableDeviceResources:
        # [out] POINTER(POINTER(IPortableDeviceResources)) ppResources
        return PortableDeviceResources(self.p.Transfer())

    def delete(self, options: int, object_ids: PortableDevicePropVariantCollection)\
            -> PortableDevicePropVariantCollection:
        options = c_ulong(options)
        # [in, out] POINTER(POINTER(IPortableDevicePropVariantCollection)) ppResults
        result = self.p.Delete(
            dwOptions = options,        # [in] c_ulong dwOptions
            pObjectIDs = object_ids.p)  # [in] POINTER(IPortableDevicePropVariantCollection) pObjectIDs
        return PortableDevicePropVariantCollection(result)
