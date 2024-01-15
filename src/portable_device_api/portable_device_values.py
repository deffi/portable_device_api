from __future__ import annotations

from ctypes import pointer, create_string_buffer, c_ubyte, cast, POINTER
from ctypes.wintypes import DWORD
from comtypes import GUID

from portable_device_api import (PortableDevicePropVariantCollection, PortableDeviceKeyCollection, PortableDeviceValuesCollection,
                     PropertyKey, IUnknown, PropVariant)
from portable_device_api._api import portable_device_types, portable_device_api
from portable_device_api._util import ComWrapper


# The parameter descriptions are from the comtypes auto-generated module

# https://learn.microsoft.com/en-us/windows/win32/wpd_sdk/iportabledevicevalues
class PortableDeviceValues(ComWrapper):
    """Essentially a mapping from PropertyKey to PropVariant"""

    # Class is only defined in portable_device_types, but the API functions are
    # in portable_device_api, so we need the interface from there.
    _type_ = portable_device_types.PortableDeviceValues
    _interface_ = portable_device_api.IPortableDeviceValues

    # Generic access ###########################################################

    def get_count(self) -> int:
        count = DWORD(0)
        self.p.GetCount(pcelt = pointer(count))  # Not [out]
        return count.value

    def get_at(self, index) -> tuple[PropertyKey, PropVariant]:
        # [in, out] POINTER(tag_inner_PROPVARIANT) pValue
        p_key, p_value = self.p.GetAt(index = index)  # [in] c_ulong
        return PropertyKey.create(p_key.fmtid, p_key.pid), PropVariant(p_value)

    def get_value(self, key: PropertyKey) -> PropVariant:
        # [out] POINTER(tag_inner_PROPVARIANT) pValue
        p_value = self.p.GetValue(key = key.v)  # [in] POINTER(_tagpropertykey) key
        return PropVariant(p_value)

    #     COMMETHOD(
    #         [],
    #         HRESULT,
    #         'GetValue',
    #         (['in'], POINTER(_tagpropertykey), 'key'),
    #         (['out'], POINTER(tag_inner_PROPVARIANT), 'pValue')
    #     ),
    #     COMMETHOD(
    #         [],
    #         HRESULT,
    #         'SetValue',
    #         (['in'], POINTER(_tagpropertykey), 'key'),
    #         (['in'], POINTER(tag_inner_PROPVARIANT), 'pValue')
    #     ),

    def remove_value(self, key: PropertyKey):
        self.p.RemoveValue(pointer(key.v))

    # Specific setters #########################################################

    def set_string_value(self, key: PropertyKey, value: str):
        # [in] WSTRING Value
        self.p.SetStringValue(key = key.v, Value = value)

    def set_unsigned_integer_value(self, key: PropertyKey, value: int):
        # [in] c_ulong Value
        self.p.SetUnsignedIntegerValue(key = key.v, Value = value)

    def set_signed_integer_value(self, key: PropertyKey, value: int):
        # [in] c_int Value
        self.p.SetSignedIntegerValue(key = key.v, Value = value)

    def set_unsigned_large_integer_value(self, key: PropertyKey, value: int):
        # [in] c_ulonglong Value
        self.p.SetUnsignedLargeIntegerValue(key = key.v, Value = value)

    def set_signed_large_integer_value(self, key: PropertyKey, value: int):
        # [in] c_longlong Value
        self.p.SetSignedLargeIntegerValue(key = key.v, Value = value)

    def set_float_value(self, key: PropertyKey, value: float):
        # [in] c_float Value
        self.p.SetFloatValue(key = key.v, Value = value)

    def set_error_value(self, key: PropertyKey, value: int):
        # [in] HRESULT Value
        self.p.SetErrorValue(key = key.v, Value = value)

    def set_key_value(self, key: PropertyKey, value: PropertyKey):
        # [in] POINTER(_tagpropertykey) Value
        self.p.SetKeyValue(key = key.v, Value = value.v)

    def set_bool_value(self, key: PropertyKey, value: bool):
        # [in] c_int Value
        self.p.SetBoolValue(key = key.v, Value = int(value))

    def set_i_unknown_value(self, key: PropertyKey, value: IUnknown):
        # [in] POINTER(IUnknown) pValue
        self.p.SetIUnknownValue(key = key.v, pValue = value.p)

    def set_guid_value(self, key: PropertyKey, value: GUID):
        # [in] POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID) Value
        self.p.SetGuidValue(key = key.v, Value = value)

    def set_buffer_value(self, key: PropertyKey, value: bytes):
        # [in] POINTER(c_ubyte) pValue
        # [in] c_ulong cbValue
        string_buffer = create_string_buffer(value)  # Copied to the interface, freed by ctypes
        self.p.SetBufferValue(key = key.v, pValue = cast(string_buffer, POINTER(c_ubyte)), cbValue = len(value))

    def set_i_portable_device_values_value(self, key: PropertyKey, value: PortableDeviceValues):
        # [in] POINTER(IPortableDeviceValues) pValue
        self.p.SetIPortableDeviceValuesValue(key = key.v, pValue = value.p)

    def set_i_portable_device_prop_variant_collection_value(self, key: PropertyKey,
                                                            value: PortableDevicePropVariantCollection):
        # [in] POINTER(IPortableDevicePropVariantCollection) pValue
        self.p.SetIPortableDevicePropVariantCollectionValue(key = key.v, pValue = value.p)

    def set_i_portable_device_key_collection_value(self, key: PropertyKey, value: PortableDeviceKeyCollection):
        # [in] POINTER(IPortableDeviceKeyCollection) pValue
        self.p.SetIPortableDeviceKeyCollectionValue(key = key.v, pValue = value.p)

    def set_i_portable_device_values_collection_value(self, key: PropertyKey, value: PortableDeviceValuesCollection):
        # [in] POINTER(IPortableDeviceValuesCollection) pValue
        self.p.SetIPortableDeviceValuesCollectionValue(key = key.v, pValue = value.p)

    # Specific getters #########################################################

    def get_string_value(self, key: PropertyKey) -> str:
        # [out] POINTER(WSTRING) pValue
        return self.p.GetStringValue(key = key.v)

    def get_unsigned_integer_value(self, key: PropertyKey) -> int:
        # [out] POINTER(c_ulong) pValue
        return self.p.GetUnsignedIntegerValue(key = key.v)

    def get_signed_integer_value(self, key: PropertyKey) -> int:
        # [out] POINTER(c_int) pValue
        return self.p.GetSignedIntegerValue(key = key.v)

    def get_unsigned_large_integer_value(self, key: PropertyKey) -> int:
        # [out] POINTER(c_ulonglong) pValue
        return self.p.GetUnsignedLargeIntegerValue(key = key.v)

    def get_signed_large_integer_value(self, key: PropertyKey) -> int:
        # [out] POINTER(c_longlong) pValue
        return self.p.GetSignedLargeIntegerValue(key = key.v)

    def get_float_value(self, key: PropertyKey) -> float:
        # [out] POINTER(c_float) pValue
        return self.p.GetFloatValue(key = key.v)

    def get_error_value(self, key: PropertyKey) -> int:
        # [out] POINTER(HRESULT) pValue
        return self.p.GetErrorValue(key = key.v)

    def get_key_value(self, key: PropertyKey) -> PropertyKey:
        # [out] POINTER(_tagpropertykey) pValue
        value = self.p.GetKeyValue(key = key.v)
        return PropertyKey(value)

    def get_bool_value(self, key: PropertyKey) -> bool:
        # [out] POINTER(c_int) pValue
        return self.p.GetBoolValue(key = key.v) != 0

    def get_i_unknown_value(self, key: PropertyKey) -> IUnknown:
        # [out] POINTER(POINTER(IUnknown)) ppValue
        return IUnknown(self.p.GetIUnknownValue(key = key.v))

    def get_guid_value(self, key: PropertyKey) -> GUID:
        # [out] POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID) pValue
        return self.p.GetGuidValue(key = key.v)

    def get_buffer_value(self, key: PropertyKey) -> bytes:
        # [out] POINTER(POINTER(c_ubyte)) ppValue
        # [out] POINTER(c_ulong) pcbValue
        buffer, length = self.p.GetBufferValue(key = key.v)
        return bytes(buffer[0:length])

    def get_i_portable_device_values_value(self, key: PropertyKey) -> PortableDeviceValues:
        # [out] POINTER(POINTER(IPortableDeviceValues)) ppValue
        return PortableDeviceValues(self.p.GetIPortableDeviceValuesValue(key = key.v))

    def get_i_portable_device_prop_variant_collection_value(self, key: PropertyKey)\
            -> PortableDevicePropVariantCollection:
        # [out] POINTER(POINTER(IPortableDevicePropVariantCollection)) ppValue
        return PortableDevicePropVariantCollection(self.p.GetIPortableDevicePropVariantCollectionValue(key = key.v))

    def get_i_portable_device_key_collection_value(self, key: PropertyKey) -> PortableDeviceKeyCollection:
        # [out] POINTER(POINTER(IPortableDeviceKeyCollection)) ppValue
        return PortableDeviceKeyCollection(self.p.GetIPortableDeviceKeyCollectionValue(key = key.v))

    def get_i_portable_device_values_collection_value(self, key: PropertyKey) -> PortableDeviceValuesCollection:
        # [out] POINTER(POINTER(IPortableDeviceValuesCollection)) ppValue
        return self.p.GetIPortableDeviceValuesCollectionValue(key = key.v)
