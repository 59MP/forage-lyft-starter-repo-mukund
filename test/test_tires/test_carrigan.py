import unittest
from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):

    def needs_service_true(self):
        tire_wear = CarriganTires([0.9, 0.8, 0.5, 0.1])
        self.assertTrue(tires.needs_service())

    def needs_service_false(self):
        tire_wear = CarriganTires([0.8, 0.7, 0.3, 0.6])
        self.assertFalse(tires.needs_service())


if __name__ == "__main__":
    unittest.main()
