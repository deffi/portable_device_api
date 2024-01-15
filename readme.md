portable_device_api
===================

A wrapper around the Windows Portable Devices (WPD) API. The WPD API can be used
to access Media Transfer Protocol (MTP) devices, like smartphones. It can also
be used to access USB drives.


Background
----------

Programming the Windows API in Python can be tricky. This package provides
Python classes with type annotations that accept regular Python types. It also
handles some details about data allocation and conversion, as well as
workarounds for some issues.

The API provided by this package closely follows the WPD API, with very little
higher-level functionality.


Example
-------

The following example shows a list of connected devices.

```python
from portable_device_api import PortableDeviceManager

manager = PortableDeviceManager.create()

print(f"{'Description':<25}{'Friendly name':<25}{'Manufacturer':<25}")
print(f"{'-----------':<25}{'-------------':<25}{'------------':<25}")

for device_id in manager.get_devices():
    description   = manager.get_device_description(device_id)
    friendly_name = manager.get_device_friendly_name(device_id)
    manufacturer  = manager.get_device_manufacturer(device_id)

    print(f"{description!r:<25}{friendly_name:<25}{manufacturer:<25}")
```


Testing
-------

Some unit tests require a device to access; it is recommended to use a USB
drive.

* Create a folder on the drive (e.g., `portable_device_api_test`)
* Run `tools/ls.py` or the example above to determine the *device description*

To run the tests, set the environment variable `PORTABLE_DEVICE_API_TEST_PATH`
to the device description and folder name, separated by a forward slash. For
example, if your device is called `MY_DRIVE`, then set the environment variable
to `MY_DRIVE/portable_device_api_test`.

Note that the device description may contain trailing spaces. They have to be
included in the environment variable.

You can also run all tests that don't require a device by invoking pytest with
`-m "not device"`.


References
----------

* [WPD API documentation](https://learn.microsoft.com/en-us/windows/win32/wpd_sdk/wpd-application-programming-interface)
* [WPD API reference](https://learn.microsoft.com/en-us/windows/win32/api/_wpdsdk/)
