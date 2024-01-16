from collections.abc import Iterator
from ctypes import c_ushort, c_ulong, create_unicode_buffer, c_wchar_p
from ctypes import pointer, POINTER, cast

from portable_device_api import errors
from portable_device_api._api import portable_device_api
from portable_device_api._util import ignore_com_error, ComWrapper


# https://learn.microsoft.com/en-us/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledevicemanager
class PortableDeviceManager(ComWrapper):
    """
    GetDeviceProperty ist not exposed because it is for vendor-defined
    properties, and we'd need a device that supports them (and the exact names
    of a property) to test it.
    """

    _type_ = portable_device_api.PortableDeviceManager

    # Device list ##############################################################

    def get_devices(self) -> Iterator[str]:
        # Determine the length by passing a null pointer for the device IDs
        _, size = self.p.GetDevices(
            pPnPDeviceIDs=POINTER(c_wchar_p)())

        # Allocate a buffer and get the device IDs
        buffer = (c_wchar_p * size)()
        self.p.GetDevices(
            pPnPDeviceIDs=cast(buffer, POINTER(c_wchar_p)),
            pcPnPDeviceIDs=pointer(c_ulong(size)))

        yield from buffer

    def get_private_devices(self) -> Iterator[str]:
        # Determine the length by passing a null pointer for the device IDs
        _, size = self.p.GetPrivateDevices(
            pPnPDeviceIDs=POINTER(c_wchar_p)())

        # Allocate a buffer and get the device IDs
        buffer = (c_wchar_p * size)()
        self.p.GetDevices(
            pPnPDeviceIDs=cast(buffer, POINTER(c_wchar_p)),
            pcPnPDeviceIDs=pointer(c_ulong(size)))

        yield from buffer

    def refresh_device_list(self):
        self.p.RefreshDeviceList()

    # Device information #######################################################

    def get_device_description(self, device_id: str) -> str:
        # Determine the length by passing a null pointer for the description
        _, size = self.p.GetDeviceDescription(
            pszPnPDeviceID=device_id,
            pDeviceDescription=POINTER(c_ushort)())

        # Allocate a buffer and get the description
        buffer = create_unicode_buffer(size)
        self.p.GetDeviceDescription(
            pszPnPDeviceID=device_id,
            pDeviceDescription=cast(buffer, POINTER(c_ushort)),
            pcchDeviceDescription=pointer(c_ulong(size)))

        return buffer.value

    @ignore_com_error(errors.ERROR_INVALID_DATA, return_value = None)
    def get_device_friendly_name(self, device_id: str) -> str:
        """If not supported by the device, use the WPD_OBJECT_NAME property of
        the device object (object ID WPD_DEVICE_OBJECT_ID)"""

        # Determine the length by passing a null pointer for the friendly name
        _, size = self.p.GetDeviceFriendlyName(
            pszPnPDeviceID=device_id,
            pDeviceFriendlyName=POINTER(c_ushort)())

        # Allocate a buffer and get the friendly name
        buffer = create_unicode_buffer(size)
        self.p.GetDeviceFriendlyName(
            pszPnPDeviceID=device_id,
            pDeviceFriendlyName=cast(buffer, POINTER(c_ushort)),
            pcchDeviceFriendlyName=pointer(c_ulong(size)))

        return buffer.value

    def get_device_manufacturer(self, device_id: str) -> str:
        # Determine the length by passing a null pointer for the manufacturer
        _, size = self.p.GetDeviceManufacturer(
            pszPnPDeviceID=device_id,
            pDeviceManufacturer=POINTER(c_ushort)())

        # Allocate a buffer and get the manufacturer
        buffer = create_unicode_buffer(size)
        self.p.GetDeviceManufacturer(
            pszPnPDeviceID=device_id,
            pDeviceManufacturer=cast(buffer, POINTER(c_ushort)),
            pcchDeviceManufacturer=pointer(c_ulong(size)))

        return buffer.value
