from portable_device_api._api import portable_device_api, portable_device_types
from portable_device_api._util import ComWrapper


# https://learn.microsoft.com/en-us/windows/win32/wpd_sdk/iportabledevicevaluescollection
class PortableDeviceValuesCollection(ComWrapper):
    # Class is only defined in portable_device_types, but the API functions are
    # in portable_device_api, so we need the interface from there.
    _type_ = portable_device_types.PortableDeviceValuesCollection
    _interface_ = portable_device_api.IPortableDeviceValuesCollection
