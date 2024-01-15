from comtypes import GUID

from portable_device_api import definitions


class TestErrors:
    def test_reverse_lookup(self):
        assert definitions.reverse_lookup[GUID("{ef2107d5-a52a-4243-a26b-62d4176d7603}")] == "WPD_CONTENT_TYPE_IMAGE"
