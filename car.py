from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery, tires):
        self.e = engine
        self.b = battery
        self.t = tires


    def needs_service(self) -> bool:
        if self.e.needs_service() or self.b.needs_service() or self.t.needs_service():
            return True
        return False
