from datetime import datetime

from pytest import approx

from portable_device_api._util.date import from_windows_date, to_windows_date

# We should probably use the Windows API to convert dates


class TestDate:
    def test_from_windows_date(self):
        assert from_windows_date(45306.782013888886) == datetime(2024, 1, 15, 18, 46, 6)

    def test_to_windows_date(self):
        # 1e-6 days ≈ 0.08 seconds
        assert to_windows_date(datetime(2024, 1, 15, 18, 46, 6)) == approx(45306.782013888886, abs = 1e-6)
