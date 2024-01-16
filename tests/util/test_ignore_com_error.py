from comtypes import COMError
import pytest

from portable_device_api._util import ignore_com_error


class TestIgnoreComError:
    def test_com_error(self):
        with pytest.raises(COMError):
            raise COMError(123, "text", (None, None, None, None, None))

    def test_context_manager(self):
        # COMError with matching HRESULT
        with ignore_com_error(123):
            raise COMError(123, "text", (None, None, None, None, None))

        # COMError with different HRESULT
        with pytest.raises(COMError):
            with ignore_com_error(123):
                raise COMError(124, "text", (None, None, None, None, None))

        # Other exception
        with pytest.raises(ValueError):
            with ignore_com_error(123):
                raise ValueError()

    def test_context_manager_with_return_value(self):
        # That's not allowed
        with pytest.raises(RuntimeError):
            with ignore_com_error(123, return_value=None):
                pass

    def test_decorator(self):
        @ignore_com_error(123, return_value="you fail")
        def function(hresult):
            raise COMError(hresult, "text", (None, None, None, None, None))

        # COMError with matching HRESULT
        function(123)

        # COMError with different HRESULT
        with pytest.raises(COMError):
            function(124)

    def test_decorator_without_return_value(self):
        # That's not allowed
        with pytest.raises(RuntimeError):
            @ignore_com_error(123)
            def function():
                pass
