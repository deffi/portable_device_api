import pytest

from portable_device_api import PortableDeviceContent


class TestComWrapper:
    def test_create_invalid(self):
        with pytest.raises(TypeError, match="^Cannot create PortableDeviceContent$"):
            PortableDeviceContent.create()
