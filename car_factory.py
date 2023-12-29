from car import Car

# from folder.module import class
# module is python file

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class CarFactory:

    @staticmethod
    def create_callipe(current_date, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        capultet_engine = CapuletEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)

        callipe = Car(engine= capultet_engine, battery= spindler_battery)

        return callipe

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)

        glissade = Car(engine= willoughby_engine, battery= spindler_battery)

        return glissade

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on: bool) -> Car:
        sternman_engine = SternmanEngine(warning_light_on)
        spindler_battery = SpindlerBattery(last_service_date, current_date)

        palindrome = Car(engine= sternman_engine, battery= spindler_battery)

        return palindrome

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)

        rorschach = Car(engine= willoughby_engine, battery= nubbin_battery)

        return rorschach

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        capultet_engine = CapuletEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)

        thovex = Car(engine= capultet_engine, battery= nubbin_battery)

        return thovex
