import comtypes.automation

from portable_device_api import PropVariant


class TestPropVariant:
    def test_default_init(self):
        p = PropVariant.create()
        assert p.v.vt == comtypes.automation.VT_EMPTY
