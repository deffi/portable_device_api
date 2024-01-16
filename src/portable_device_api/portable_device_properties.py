from ctypes import pointer

from portable_device_api import PortableDeviceValues, PortableDeviceKeyCollection, PropertyKey
from portable_device_api._util import ComWrapper


# https://learn.microsoft.com/en-us/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledeviceproperties
class PortableDeviceProperties(ComWrapper):
    def get_values(self, object_id: str, keys: PortableDeviceKeyCollection) -> PortableDeviceValues:
        # [out] POINTER(POINTER(IPortableDeviceValues)) ppValues
        return PortableDeviceValues(self.p.GetValues(
            pszObjectID = object_id,  # [in] WSTRING
            pKeys = keys.p))          # [in] POINTER(IPortableDeviceKeyCollection)

    def get_supported_properties(self, object_id: str) -> PortableDeviceKeyCollection:
        # [out] POINTER(POINTER(IPortableDeviceKeyCollection)) ppKeys
        p = self.p.GetSupportedProperties(pszObjectID = object_id)  # [in] WSTRING
        return PortableDeviceKeyCollection(p)

    def get_property_attributes(self, object_id: str, key: PropertyKey) -> PortableDeviceValues:
        # [out] POINTER(POINTER(IPortableDeviceValues)) 'ppAttributes'
        p = self.p.GetPropertyAttributes(
            pszObjectID = object_id,  # [in] WSTRING
            key = pointer(key.v),     # [in] POINTER(_tagpropertykey)
        )
        return PortableDeviceValues(p)

#     COMMETHOD(
#         [],
#         HRESULT,
#         'SetValues',
#         (['in'], WSTRING, 'pszObjectID'),
#         (['in'], POINTER(IPortableDeviceValues), 'pValues'),
#         (['out'], POINTER(POINTER(IPortableDeviceValues)), 'ppResults')
#     ),
#     COMMETHOD(
#         [],
#         HRESULT,
#         'Delete',
#         (['in'], WSTRING, 'pszObjectID'),
#         (['in'], POINTER(IPortableDeviceKeyCollection), 'pKeys')
#     ),

    def cancel(self) -> None:
        self.p.Cancel()
