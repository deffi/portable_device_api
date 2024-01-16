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
        # [in, out] POINTER(WSTRING) pPnPDeviceIDs
        # [in, out] POINTER(c_ulong) pcPnPDeviceIDs
        _, size = self.p.GetDevices(
            pPnPDeviceIDs=POINTER(c_wchar_p)())  # [in, out] POINTER(WSTRING) pPnPDeviceIDs

        # Allocate a buffer and get the device IDs
        buffer = (c_wchar_p * size)()
        self.p.GetDevices(
            pPnPDeviceIDs=cast(buffer, POINTER(c_wchar_p)),  # [in, out] POINTER(WSTRING) pPnPDeviceIDs
            pcPnPDeviceIDs=pointer(c_ulong(size)))           # [in, out] POINTER(c_ulong) pcPnPDeviceIDs

        yield from buffer

    def get_private_devices(self) -> Iterator[str]:
        # Determine the length by passing a null pointer for the device IDs
        # [in, out] POINTER(WSTRING) pPnPDeviceIDs
        # [in, out] POINTER(c_ulong) pcPnPDeviceIDs
        _, size = self.p.GetPrivateDevices(
            pPnPDeviceIDs=POINTER(c_wchar_p)())  # [in, out] POINTER(WSTRING) pPnPDeviceIDs

        # Allocate a buffer and get the device IDs
        buffer = (c_wchar_p * size)()
        self.p.GetDevices(
            pPnPDeviceIDs=cast(buffer, POINTER(c_wchar_p)),  # [in, out] POINTER(WSTRING) pPnPDeviceIDs
            pcPnPDeviceIDs=pointer(c_ulong(size)))           # [in, out] POINTER(c_ulong) pcPnPDeviceIDs

        yield from buffer

    def refresh_device_list(self):
        self.p.RefreshDeviceList()

    # Device information #######################################################

    def get_device_description(self, device_id: str) -> str:
        # Determine the length by passing a null pointer for the description
        # [in, out] POINTER(c_ushort) pDeviceDescription
        # [in, out] POINTER(c_ulong) pcchDeviceDescription
        _, size = self.p.GetDeviceDescription(
            pszPnPDeviceID=device_id,                # [in] WSTRING pszPnPDeviceID
            pDeviceDescription=POINTER(c_ushort)())  # [in, out] POINTER(c_ushort) pDeviceDescription

        # Allocate a buffer and get the description
        buffer = create_unicode_buffer(size)
        self.p.GetDeviceDescription(
            pszPnPDeviceID=device_id,                            # [in] WSTRING pszPnPDeviceID
            pDeviceDescription=cast(buffer, POINTER(c_ushort)),  # [in, out] POINTER(c_ushort) pDeviceDescription
            pcchDeviceDescription=pointer(c_ulong(size)))        # [in, out] POINTER(c_ulong) pcchDeviceDescription

        return buffer.value

    @ignore_com_error(errors.ERROR_INVALID_DATA, return_value = None)
    def get_device_friendly_name(self, device_id: str) -> str:
        """If not supported by the device, use the WPD_OBJECT_NAME property of
        the device object (object ID WPD_DEVICE_OBJECT_ID)"""

        # Determine the length by passing a null pointer for the friendly name
        # [in, out] POINTER(c_ushort) pDeviceFriendlyName
        # [in, out] POINTER(c_ulong) pcchDeviceFriendlyName
        _, size = self.p.GetDeviceFriendlyName(
            pszPnPDeviceID=device_id,                 # [in] WSTRING pszPnPDeviceID
            pDeviceFriendlyName=POINTER(c_ushort)())  # [in, out] POINTER(c_ushort) pDeviceFriendlyName

        # Allocate a buffer and get the friendly name
        buffer = create_unicode_buffer(size)
        self.p.GetDeviceFriendlyName(
            pszPnPDeviceID=device_id,                             # [in] WSTRING pszPnPDeviceID
            pDeviceFriendlyName=cast(buffer, POINTER(c_ushort)),  # [in, out] POINTER(c_ushort) pDeviceFriendlyName
            pcchDeviceFriendlyName=pointer(c_ulong(size)))        # [in, out] POINTER(c_ulong) pcchDeviceFriendlyName

        return buffer.value

    def get_device_manufacturer(self, device_id: str) -> str:
        # Determine the length by passing a null pointer for the manufacturer
        # [in, out] POINTER(c_ushort) pDeviceManufacturer
        # [in, out] POINTER(c_ulong) pcchDeviceManufacturer
        _, size = self.p.GetDeviceManufacturer(
            pszPnPDeviceID=device_id,                 # [in] WSTRING pszPnPDeviceID
            pDeviceManufacturer=POINTER(c_ushort)())  # [in, out] POINTER(c_ushort) pDeviceManufacturer

        # Allocate a buffer and get the manufacturer
        buffer = create_unicode_buffer(size)
        self.p.GetDeviceManufacturer(
            pszPnPDeviceID=device_id,                             # [in] WSTRING pszPnPDeviceID
            pDeviceManufacturer=cast(buffer, POINTER(c_ushort)),  # [in, out] POINTER(c_ushort) pDeviceManufacturer
            pcchDeviceManufacturer=pointer(c_ulong(size)))        # [in, out] POINTER(c_ulong) pcchDeviceManufacturer

        return buffer.value
