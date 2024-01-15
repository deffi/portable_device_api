from comtypes.client import GetModule as _GetModule

_module = _GetModule("portabledevicetypes.dll")

PortableDeviceValues = _module.PortableDeviceValues
PortableDeviceKeyCollection = _module.PortableDeviceKeyCollection
PortableDeviceValuesCollection = _module.PortableDeviceValuesCollection
PortableDevicePropVariantCollection = _module.PortableDevicePropVariantCollection

# We also have the same type in portable_device_api, but it seems like the
# methods in each library require the tag_inner_PROPVARIANT from the same
# library. We may have to convert between the two.
tag_inner_PROPVARIANT = _module.tag_inner_PROPVARIANT
