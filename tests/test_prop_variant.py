import comtypes.automation
import pytest

from portable_device_api import PropVariant


class TestPropVariant:
    def test_default_init(self):
        p = PropVariant.create()
        assert p.v.vt == comtypes.automation.VT_EMPTY

    def test_unhandled_vt(self):
        p = PropVariant.create(comtypes.automation.VT_USERDEFINED)

        with pytest.raises(ValueError):
            p.value = 0

        with pytest.raises(ValueError):
            _ = p.value
