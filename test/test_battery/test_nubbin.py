from battery.nubbin_battery import NubbinBattery
from datetime import datetime
import unittest


class test_nubbin_battery(unittest.TestCase):

    def test_needs_service_true(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())


    def test_needs_service_false(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

if __name__ == "__main__":
    unittest.main()
