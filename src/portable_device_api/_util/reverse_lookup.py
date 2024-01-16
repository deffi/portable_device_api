from collections.abc import Mapping
from typing import TypeVar

KT = TypeVar("KT")
VT = TypeVar("VT")
DT = TypeVar("DT")


class ReverseLookup:
    def __init__(self, mapping: Mapping[KT, VT]):
        # Note that some values might not be hashable, so we can't use a dict
        self._items = list(mapping.items())

    def __getitem__(self, value: VT) -> KT:
        for k, v in self._items:
            if v == value:
                return k
        else:
            raise KeyError(value)

    def get(self, value: VT, default_key: DT = None) -> KT | DT:
        try:
            return self[value]
        except KeyError:
            return default_key
