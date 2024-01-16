from collections.abc import Iterator
import os
from datetime import datetime

import pytest

from comtypes.automation import VT_LPWSTR

from portable_device_api import (errors, PropVariant, PortableDeviceManager, PortableDevice, PortableDevicePropVariantCollection,
                     PortableDeviceValues, PortableDeviceKeyCollection)
import portable_device_api.definitions as defs


timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


class TestDevice:
    def __init__(self, device_description: str):
        self.test_dir_object_id = None

        manager = PortableDeviceManager.create()

        manager.refresh_device_list()

        list(manager.get_private_devices())

        device_ids = list(manager.get_devices())
        device_descriptions = [manager.get_device_description(did) for did in device_ids]
        device_friendly_names = [manager.get_device_friendly_name(did) for did in device_ids]
        device_manufacturers = [manager.get_device_manufacturer(did) for did in device_ids]
        matching_device_ids = [did for did in device_ids if manager.get_device_description(did) == device_description]
        assert len(matching_device_ids) == 1
        device_id = matching_device_ids[0]

        self.device = PortableDevice.create()
        self.device.open(device_id)
        self.content = self.device.content()
        self.resource = self.content.transfer()
        self.properties = self.content.properties()

    def setup(self, base_dir: str) -> None:
        root_object_id = self.content.enum_objects(defs.WPD_DEVICE_OBJECT_ID).next(1)[0]

        top_object_ids = self.content.enum_objects(root_object_id).next(999)
        keys = PortableDeviceKeyCollection.create()
        keys.add(defs.WPD_OBJECT_ORIGINAL_FILE_NAME)
        matching_object_ids = [oid for oid in top_object_ids if self.properties.get_values(oid, keys).get_string_value(
            defs.WPD_OBJECT_ORIGINAL_FILE_NAME) == base_dir]
        assert len(matching_object_ids) == 1
        base_object_id = matching_object_ids[0]

        values = PortableDeviceValues.create()
        values.set_guid_value(defs.WPD_OBJECT_CONTENT_TYPE, defs.WPD_CONTENT_TYPE_FOLDER)
        values.set_string_value(defs.WPD_OBJECT_PARENT_ID, base_object_id)
        values.set_string_value(defs.WPD_OBJECT_NAME, timestamp)

        self.test_dir_object_id = self.content.create_object_with_properties_only(values)

    def cleanup(self) -> None:
        object_ids_pvc = PortableDevicePropVariantCollection.create()
        object_ids_pvc.add(PropVariant.create(VT_LPWSTR, self.test_dir_object_id))
        self.content.delete(defs.DELETE_OBJECT_OPTIONS.PORTABLE_DEVICE_DELETE_NO_RECURSION, object_ids_pvc)

    # High-level functionality

    def find_object_id(self, parent_object_id: str, object_name: str) -> str | None:
        object_ids = self.content.enum_objects(parent_object_id).next(999)
        for object_id in object_ids:
            if self.get_object_name(object_id) == object_name:
                return object_id
        else:
            return None

    def get_object_names(self, object_id = None) -> list[str]:
        object_id = object_id or self.test_dir_object_id

        children = self.content.enum_objects(object_id).next(999)
        return [self.get_object_name(oid) for oid in children]

    def get_object_name(self, object_id: str) -> str:
        keys = PortableDeviceKeyCollection.create()
        keys.add(defs.WPD_OBJECT_ORIGINAL_FILE_NAME)
        return self.properties.get_values(object_id, keys).get_string_value(defs.WPD_OBJECT_ORIGINAL_FILE_NAME)

    def create_directory(self, parent_object_id: str, dir_name: str) -> str:
        """object_id"""
        values = PortableDeviceValues.create()
        values.set_guid_value(defs.WPD_OBJECT_CONTENT_TYPE, defs.WPD_CONTENT_TYPE_FOLDER)
        values.set_string_value(defs.WPD_OBJECT_PARENT_ID, parent_object_id)
        values.set_string_value(defs.WPD_OBJECT_NAME, dir_name)

        return self.content.create_object_with_properties_only(values)

    def delete(self, object_ids: list[str], recursive: bool) -> list[int]:
        object_ids_pvc = PortableDevicePropVariantCollection.create()
        for object_id in object_ids:
            object_ids_pvc.add(PropVariant.create(VT_LPWSTR, object_id))

        if recursive:
            flags = defs.DELETE_OBJECT_OPTIONS.PORTABLE_DEVICE_DELETE_WITH_RECURSION
        else:
            flags = defs.DELETE_OBJECT_OPTIONS.PORTABLE_DEVICE_DELETE_NO_RECURSION

        delete_result = self.content.delete(flags, object_ids_pvc)
        return [errors.to_hresult(delete_result.get_at(i).value) for i in range(delete_result.get_count())]

    def upload_file(self, parent_object_id: str, file_name: str, content: bytes) -> str:
        values = PortableDeviceValues.create()
        values.set_string_value(defs.WPD_OBJECT_PARENT_ID, parent_object_id)
        values.set_unsigned_large_integer_value(defs.WPD_OBJECT_SIZE, len(content))
        values.set_string_value(defs.WPD_OBJECT_ORIGINAL_FILE_NAME, file_name)
        values.set_string_value(defs.WPD_OBJECT_NAME, file_name)

        stream, chunk_size = self.content.create_object_with_properties_and_data(values)
        buffer = bytearray(content)
        while buffer:
            this_chunk_size = min(len(buffer), chunk_size)
            chunk = buffer[0:this_chunk_size]
            buffer[0:this_chunk_size] = []
            stream.remote_write(chunk)
        stream.commit()

        return stream.get_object_id()

    def download_file(self, object_id: str) -> bytes:
        stream, optimal_transfer_size = self.resource.get_stream(object_id)
        buffer = bytearray()
        while chunk := stream.remote_read(optimal_transfer_size):
            buffer.extend(chunk)
        return buffer


@pytest.fixture(scope = "session")
def test_device():
    device_description, base_name = os.environ["PORTABLE_DEVICE_API_TEST_PATH"].split("/")
    td = TestDevice(device_description)
    td.setup(base_name)
    yield td
    td.cleanup()


class TestWpdApi:
    @pytest.mark.device
    def test_create_remove_dir(self, test_device):
        dir_name = "test_dir"
        assert dir_name not in test_device.get_object_names()

        object_id = test_device.create_directory(test_device.test_dir_object_id, dir_name)
        assert dir_name in test_device.get_object_names()

        # Remove the directory
        delete_result = test_device.delete([object_id], False)
        assert delete_result == [0]
        assert dir_name not in test_device.get_object_names()

        # Remove the directory again (it's missing now)
        delete_result = test_device.delete([object_id], False)
        assert delete_result == [errors.ERROR_FILE_NOT_FOUND]
        assert dir_name not in test_device.get_object_names()

    @pytest.mark.device
    def test_upload_download_remove_file(self, test_device):
        content = "hello\nportable_device_api\ntest".encode()
        file_name = "upload.txt"
        assert file_name not in test_device.get_object_names()

        # Create the file
        object_id = test_device.upload_file(test_device.test_dir_object_id, file_name, content)
        assert file_name in test_device.get_object_names()
        assert object_id == test_device.find_object_id(test_device.test_dir_object_id, file_name)

        # Download the file
        assert test_device.download_file(object_id) == content
        assert file_name in test_device.get_object_names()

        # Remove the file
        delete_result = test_device.delete([object_id], False)
        assert delete_result == [0]
        assert file_name not in test_device.get_object_names()

        # Remove the file again (it's missing now)
        delete_result = test_device.delete([object_id], False)
        assert delete_result == [errors.ERROR_FILE_NOT_FOUND]
        assert file_name not in test_device.get_object_names()

    @pytest.mark.device
    def test_download_cancel(self, test_device):
        content = "hello\nportable_device_api\ntest".encode()
        file_name = "upload.txt"

        # Create the file
        object_id = test_device.upload_file(test_device.test_dir_object_id, file_name, content)
        assert test_device.download_file(object_id) == content

        stream, optimal_transfer_size = test_device.resource.get_stream(object_id)
        stream.remote_read(1)
        stream.cancel()  # Does not seem necessary
        del stream       # Seems necessary

        # Remove the file
        delete_result = test_device.delete([object_id], False)
        assert delete_result == [0]
        assert file_name not in test_device.get_object_names()

    @pytest.mark.device
    def test_recursive_delete(self, test_device):
        dir_name = "foo"
        assert dir_name not in test_device.get_object_names()

        object_id = test_device.create_directory(test_device.test_dir_object_id, dir_name)
        test_device.upload_file(object_id, "bar", b"bar")
        assert dir_name in test_device.get_object_names()

        assert test_device.delete([object_id], False) == [errors.ERROR_DIR_NOT_EMPTY]
        assert dir_name in test_device.get_object_names()

        assert test_device.delete([object_id], True) == [0]
        assert dir_name not in test_device.get_object_names()

    @pytest.mark.device
    def test_properties(self, test_device):
        supported_properties = test_device.properties.get_supported_properties(test_device.test_dir_object_id)
        supported_properties = [supported_properties.get_at(i) for i in range(supported_properties.get_count())]
        assert defs.WPD_OBJECT_CONTENT_TYPE in supported_properties
        assert defs.WPD_OBJECT_DATE_CREATED in supported_properties

        keys = PortableDeviceKeyCollection.create()
        keys.add(defs.WPD_OBJECT_CONTENT_TYPE)
        keys.add(defs.WPD_OBJECT_DATE_CREATED)
        values = test_device.properties.get_values(test_device.test_dir_object_id, keys)
        assert values.get_guid_value(defs.WPD_OBJECT_CONTENT_TYPE) == defs.WPD_CONTENT_TYPE_FOLDER  # Direct
        assert values.get_value(defs.WPD_OBJECT_CONTENT_TYPE).value == defs.WPD_CONTENT_TYPE_FOLDER  # Via PropVariant
        # IPortableDeviceValues has not getter for date, use the PropVariant
        date_created = values.get_value(defs.WPD_OBJECT_DATE_CREATED).value    # Via PropVariant
        assert isinstance(date_created, datetime)
        assert abs(date_created - datetime.now()).total_seconds() < 60  # Less than a minute

    @pytest.mark.device
    def test_property_attributes(self, test_device):
        attributes = test_device.properties.get_property_attributes(test_device.test_dir_object_id,
                                                                    defs.WPD_OBJECT_CONTENT_TYPE)
        assert attributes.get_value(defs.WPD_PROPERTY_ATTRIBUTE_CAN_READ).value is True
        assert attributes.get_value(defs.WPD_PROPERTY_ATTRIBUTE_CAN_WRITE).value is False
