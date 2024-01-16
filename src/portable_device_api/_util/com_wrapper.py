from typing import Self

import comtypes.client


class ComWrapper:
    _type_ = None
    _interface_ = None

    def __init__(self, p):
        # Example:
        #     type(self).__name__ = "PortableDeviceManager"
        #     # repr(p) = <POINTER(IPortableDeviceManager) ptr=0x... at ...>
        assert type(self).__name__.lower() in repr(p).lower()

        self._p = p

    @classmethod
    def create(cls) -> Self:
        if cls._type_ is not None:
            return cls(comtypes.client.CreateObject(
                progid = cls._type_,
                clsctx = comtypes.CLSCTX_INPROC_SERVER,
                interface = cls._interface_))
        else:
            raise TypeError(f"Cannot create {cls.__name__}")

    @property
    def p(self):
        return self._p
