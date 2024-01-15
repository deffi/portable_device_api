from datetime import datetime, timedelta

_base = datetime(1899, 12, 30, 0, 0, 0)


def from_windows_date(value: float) -> datetime:
    return _base + timedelta(days = value)


def to_windows_date(value: datetime) -> float:
    return (value - _base).total_seconds() / 86400
