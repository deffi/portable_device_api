from comtypes import GUID

from portable_device_api import PortableDeviceKeyCollection, PropertyKey


class TestPortableDeviceKeyCollection:
    def test_add_clear_get_count(self):
        uut = PortableDeviceKeyCollection.create()
        assert uut.get_count() == 0
        uut.add(PropertyKey.create(GUID("{00000000-0000-0000-0000-000000000000}"), 0))
        assert uut.get_count() == 1
        uut.add(PropertyKey.create(GUID("{00000000-0000-0000-0000-000000000000}"), 0))  # Same thing again
        assert uut.get_count() == 2
        uut.clear()
        assert uut.get_count() == 0

    def test_get_at(self):
        uut = PortableDeviceKeyCollection.create()
        uut.add(PropertyKey.create(GUID("{DEADBEEF-0000-0000-0000-000000000000}"), 11))
        uut.add(PropertyKey.create(GUID("{BADEAFFE-0000-0000-0000-000000000000}"), 22))

        assert uut.get_at(1) == PropertyKey.create(GUID("{BADEAFFE-0000-0000-0000-000000000000}"), 22)
        assert uut.get_at(0) == PropertyKey.create(GUID("{DEADBEEF-0000-0000-0000-000000000000}"), 11)

    def test_remove_at(self):
        uut = PortableDeviceKeyCollection.create()
        uut.add(PropertyKey.create(GUID("{DEADBEEF-0000-0000-0000-000000000000}"), 11))
        uut.add(PropertyKey.create(GUID("{BADEAFFE-0000-0000-0000-000000000000}"), 22))
        uut.remove_at(0)
        assert uut.get_at(0) == PropertyKey.create(GUID("{BADEAFFE-0000-0000-0000-000000000000}"), 22)
