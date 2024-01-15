from collections.abc import Mapping

UNSPECIFIED = object()


class ReverseLookup:
    def __init__(self, mapping: Mapping):
        # Note that some values might not be hashable, so we can't use a dict
        self._items = list(mapping.items())

    def __getitem__(self, value):
        for k, v in self._items:
            if v == value:
                return k
        else:
            raise KeyError(value)

    def get(self, value, default_key = None):
        try:
            return self[value]
        except KeyError:
            return default_key
