from comtypes import GUID

from portable_device_api import PortableDeviceKeyCollection, PropertyKey


class TestPortableDeviceKeyCollection:
    def test_add_clear_get_count(self):
        uut = PortableDeviceKeyCollection.create()
        assert uut.get_count() == 0
        uut.add(PropertyKey.create(fmtid=GUID("{00000000-0000-0000-0000-000000000000}"), pid=0))
        assert uut.get_count() == 1
        uut.add(PropertyKey.create(fmtid=GUID("{00000000-0000-0000-0000-000000000000}"), pid=0))  # Same thing again
        assert uut.get_count() == 2
        uut.clear()
        assert uut.get_count() == 0

    def test_get_at(self):
        uut = PortableDeviceKeyCollection.create()
        uut.add(PropertyKey.create(fmtid=GUID("{DEADBEEF-0000-0000-0000-000000000000}"), pid=11))
        uut.add(PropertyKey.create(fmtid=GUID("{BADEAFFE-0000-0000-0000-000000000000}"), pid=22))

        assert uut.get_at(1) == PropertyKey.create(fmtid=GUID("{BADEAFFE-0000-0000-0000-000000000000}"), pid=22)
        assert uut.get_at(0) == PropertyKey.create(fmtid=GUID("{DEADBEEF-0000-0000-0000-000000000000}"), pid=11)

    def test_remove_at(self):
        uut = PortableDeviceKeyCollection.create()
        uut.add(PropertyKey.create(fmtid=GUID("{DEADBEEF-0000-0000-0000-000000000000}"), pid=11))
        uut.add(PropertyKey.create(fmtid=GUID("{BADEAFFE-0000-0000-0000-000000000000}"), pid=22))
        uut.remove_at(0)
        assert uut.get_at(0) == PropertyKey.create(fmtid=GUID("{BADEAFFE-0000-0000-0000-000000000000}"), pid=22)
