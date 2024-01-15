from portable_device_api import errors


class TestErrors:
    def test_reverse_lookup(self):
        assert errors.reverse_lookup[0x800700AA] == "ERROR_BUSY"

    def test_to_hresult(self):
        assert errors.to_hresult(-0x7FF8FFFB) == 0x80070005
        assert errors.to_hresult(0x80070005) == 0x80070005
