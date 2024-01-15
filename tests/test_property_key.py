from comtypes import GUID

from portable_device_api import PropertyKey
from portable_device_api._api.portable_device_api import tagpropertykey


class TestPropertyKey:
    def test_create(self):
        a = PropertyKey.create(fmtid=GUID("{EF6B490D-5CD8-437A-AFFC-DA8B60EE4A3C}"), pid=7)
        assert a.v.fmtid == GUID("{EF6B490D-5CD8-437A-AFFC-DA8B60EE4A3C}")
        assert a.v.pid == 7

    def test_equality(self):
        a = PropertyKey.create(fmtid=GUID("{EF6B490D-5CD8-437A-AFFC-DA8B60EE4A3C}"), pid=7)
        b = PropertyKey.create(fmtid=GUID("{EF6B490D-5CD8-437A-AFFC-DA8B60EE4A3C}"), pid=7)
        assert a is not b
        assert a == b
        assert b == a

    def test_equality_from_tagpropertykey(self):
        a = PropertyKey.create(fmtid=GUID("{EF6B490D-5CD8-437A-AFFC-DA8B60EE4A3C}"), pid=7)
        b = PropertyKey(tagpropertykey(fmtid=GUID("{EF6B490D-5CD8-437A-AFFC-DA8B60EE4A3C}"), pid=7))
        assert a is not b
        assert a == b
        assert b == a
