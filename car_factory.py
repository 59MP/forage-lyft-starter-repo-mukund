from car import Car
# from folder.module import class
# module is python file
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class CarFactory:

    @staticmethod
    def create_callipe(current_date, last_service_date, current_mileage: int, last_service_mileage: int, tire_wear) -> Car:
        tires = CarriganTires(tire_wear)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)

        callipe = Car(engine, battery, tires)

        return callipe

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage: int, last_service_mileage: int, tire_wear) -> Car:
        tires = OctoprimeTires(tire_wear)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)

        glissade = Car(engine, battery, tires)

        return glissade

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on: bool, tire_wear) -> Car:
        tires = CarriganTires(tire_wear)
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)

        palindrome = Car(engine, battery, tires)

        return palindrome

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage: int, last_service_mileage: int, tire_wear) -> Car:
        tires = OctoprimeTires(tire_wear)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)

        rorschach = Car(engine, battery, tires)

        return rorschach

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage: int, last_service_mileage: int, tire_wear) -> Car:
        tires = CarriganTires(tire_wear)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)

        thovex = Car(engine, battery, tires)

        return thovex
