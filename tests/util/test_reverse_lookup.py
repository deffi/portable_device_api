import pytest

from portable_device_api._util import ReverseLookup


class TestReverseLookup:
    @pytest.mark.parametrize("value, expected_key", [
        ([11, 111], "l"),
        ((11, 111), "t"),
    ])
    def test_getitem(self, value, expected_key):
        m = {"l": [11, 111], "t": (11, 111)}
        assert ReverseLookup(m)[value] == expected_key

    def test_getitem_index_error(self):
        m = {"l": [11, 111], "t": (11, 111)}
        with pytest.raises(KeyError):
            _ = ReverseLookup(m)[{11, 111}]

    @pytest.mark.parametrize("value, expected_key", [
        ([11, 111], "l"),
        ((11, 111), "t"),
        ({11, 111}, "?"),
    ])
    def test_get(self, value, expected_key):
        m = {"l": [11, 111], "t": (11, 111)}
        assert ReverseLookup(m).get(value, "?") == expected_key
