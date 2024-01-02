import unittest
from tires.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):

    def needs_service_true(self):
        tire_wear = OctoprimeTires([0.5, 0.3, 0.1, 2.2])
        self.assertTrue(tires.needs_service())

    def needs_service_false(self):
        tire_wear = OctoprimeTires([0.8, 0.9, 1, 0.1])
        self.assertFalse(tires.needs_service())


if __name__ == "__main__":
    unittest.main()
