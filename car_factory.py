from car import Car
from engine import Engine
from battery import Battery

class CarFactory:

    def create_callipe(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        capultet_engine = CapuletEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)

        callipe = Car(engine= capultet_engine, battery= spindler_battery)

        return callipe

    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)

        glissade = Car(engine= willoughby_engine, battery= spindler_battery)

        return glissade

    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        sternman_engine = SternmanEngine(warning_light_on)
        spindler_battery = SpindlerBattery(last_service_date, current_date)

        palindrome = Car(engine= sternman_engine, battery= spindler_battery)

        return palindrome

    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)

        rorschach = Car(engine= willoughby_engine, battery= nubbin_battery)

        return rorschach

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        capultet_engine = CapuletEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)

        thovex = Car(engine= capultet_engine, battery= nubbin_battery)

        return thovex
