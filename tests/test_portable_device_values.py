import pytest
from comtypes import GUID, COMError

from pytest import approx

from portable_device_api.errors import to_hresult
from portable_device_api import PortableDeviceValues, PropertyKey


Uut = PortableDeviceValues
guid_1 = GUID("{DEADBEEF-0000-0000-0000-000000000000}")
guid_2 = GUID("{BADEAFFE-0000-0000-0000-000000000000}")

key_11 = PropertyKey.create(guid_1, 1)
key_22 = PropertyKey.create(guid_2, 2)


class TestPortableDeviceValues:
    def test_get_count(self):
        uut = PortableDeviceValues.create()
        assert uut.get_count() == 0
        uut.set_string_value(key_11, "twelve")
        assert uut.get_count() == 1
        uut.set_string_value(key_11, "dozen")  # Same
        assert uut.get_count() == 1  # Still 1
        uut.set_string_value(key_22, "thirteen")  # Different
        assert uut.get_count() == 2

        uut.remove_value(key_11)
        assert uut.get_count() == 1

        uut.remove_value(key_22)
        assert uut.get_count() == 0

    # Specific setters/getters #########################################################

    @staticmethod
    def _test_set_get(setter, getter, values, read_map = lambda x: x):
        uut = PortableDeviceValues.create()
        assert uut.get_count() == 0

        for index, write_value in enumerate(values):
            setter(uut, PropertyKey.create(guid_1, index), write_value)
            assert uut.get_count() == index + 1

        for index, expected_value in enumerate(values):
            read_value = getter(uut, PropertyKey.create(guid_1, index))
            assert read_map(read_value) == expected_value
            assert type(read_value) is type(expected_value)

    def test_string_value(self):
        self._test_set_get(Uut.set_string_value, Uut.get_string_value, ["one", "two"])

    def test_unsigned_integer_value(self):
        self._test_set_get(Uut.set_unsigned_integer_value, Uut.get_unsigned_integer_value, [1, 2])

    def test_signed_integer_value(self):
        self._test_set_get(Uut.set_signed_integer_value, Uut.get_signed_integer_value, [1, -2])

    def test_unsigned_large_integer_value(self):
        self._test_set_get(Uut.set_unsigned_large_integer_value, Uut.get_unsigned_large_integer_value, [1, 2])

    def test_signed_large_integer_value(self):
        self._test_set_get(Uut.set_signed_large_integer_value, Uut.get_signed_large_integer_value, [1, -2])

    def test_float_value(self):
        self._test_set_get(Uut.set_float_value, Uut.get_float_value, [1.2, 2.3], read_map = approx)

    def test_error_value(self):
        self._test_set_get(Uut.set_error_value, Uut.get_error_value, [0x80070091, 0x800710D2], read_map = to_hresult)

    def test_key_value(self):
        self._test_set_get(Uut.set_key_value, Uut.get_key_value, [key_11, key_22])

    def test_bool_value(self):
        self._test_set_get(Uut.set_bool_value, Uut.get_bool_value, [True, False, True])

    # Probably works the same as portable_device_values_value
    # def test_i_unknown_value(self):
    #     ...

    def test_guid_value(self):
        self._test_set_get(Uut.set_guid_value, Uut.get_guid_value, [guid_1, guid_2])

    def test_buffer_value(self):
        self._test_set_get(Uut.set_buffer_value, Uut.get_buffer_value, [b'foo', b'bar'])

    def test_i_portable_device_values_value(self):
        write_value_1 = PortableDeviceValues.create()
        write_value_2 = PortableDeviceValues.create()
        write_value_1.set_unsigned_integer_value(key_11, 111)
        write_value_1.set_unsigned_integer_value(key_22, 122)
        write_value_2.set_unsigned_integer_value(key_11, 211)
        write_value_2.set_unsigned_integer_value(key_22, 222)

        uut = PortableDeviceValues.create()
        uut.set_i_portable_device_values_value(key_11, write_value_1)
        uut.set_i_portable_device_values_value(key_22, write_value_2)

        read_value_1 = uut.get_i_portable_device_values_value(key_11)
        read_value_2 = uut.get_i_portable_device_values_value(key_22)

        assert read_value_1 is not write_value_1
        assert read_value_2 is not write_value_2

        assert read_value_1.get_unsigned_integer_value(key_11) == write_value_1.get_unsigned_integer_value(key_11)
        assert read_value_1.get_unsigned_integer_value(key_22) == write_value_1.get_unsigned_integer_value(key_22)
        assert read_value_2.get_unsigned_integer_value(key_11) == write_value_2.get_unsigned_integer_value(key_11)
        assert read_value_2.get_unsigned_integer_value(key_22) == write_value_2.get_unsigned_integer_value(key_22)

    # Probably works the same as portable_device_values_value
    # def test_i_portable_device_prop_variant_collection_value(self):
    #     ...

    # Probably works the same as portable_device_values_value
    # def test_i_portable_device_key_collection_value(self):
    #     ...

    # Probably works the same as portable_device_values_value
    # def test_i_portable_device_values_collection_value(self):
    #     ...

    def test_set_get_wrong_type(self):
        uut = PortableDeviceValues.create()

        # If the value represents a valid GUID, we can get it as a GUID
        uut.set_string_value(key_11, "{DEADBEEF-0000-0000-0000-000000000000}")
        assert uut.get_string_value(key_11) == "{DEADBEEF-0000-0000-0000-000000000000}"
        assert uut.get_guid_value(key_11) == GUID("{DEADBEEF-0000-0000-0000-000000000000}")

        # Otherwise, we get an exception
        uut.set_string_value(key_22, "foo")
        assert uut.get_string_value(key_22) == "foo"
        with pytest.raises(COMError):
            uut.get_guid_value(key_22)
