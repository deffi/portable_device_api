from functools import wraps

from comtypes import COMError

from portable_device_api import errors

UNSPECIFIED = object()


class ignore_com_error:
    def __init__(self, hresult: int, *, return_value = UNSPECIFIED):
        self._hresult = hresult
        self._return_value = return_value

    def _ignore_error(self, e: Exception) -> bool:
        if isinstance(e, COMError):
            return errors.to_hresult(e.hresult) == self._hresult
        else:
            return False

    def __enter__(self):  # Context manager
        if self._return_value is not UNSPECIFIED:
            raise RuntimeError("ignore_com_error with return value cannot be used as a context manager")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # Context manager
        if self._ignore_error(exc_val):
            return True  # Ignore exception

    def __call__(self, func):  # Decorator
        if self._return_value is UNSPECIFIED:
            raise RuntimeError("ignore_com_error with return value cannot be used as a decorator")

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if self._ignore_error(e):
                    return self._return_value
                else:
                    raise

        return wrapper


