from portable_device_api import PortableDeviceContent
from portable_device_api import PortableDeviceValues
from portable_device_api._api import portable_device_api
from portable_device_api._util import ComWrapper


# https://learn.microsoft.com/en-us/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledevice
class PortableDevice(ComWrapper):
    _type_ = portable_device_api.PortableDevice

    # Connection ###############################################################

    def open(self, device_id: str):
        client_information = PortableDeviceValues.create()
        self.p.Open(
            pszPnPDeviceID = device_id,
            pClientInfo = client_information.p)

    def close(self):
        self.p.Close()

    # Content ##################################################################

    def content(self) -> PortableDeviceContent:
        return PortableDeviceContent(self.p.Content())
