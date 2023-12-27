from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: battery):
        self.engine = e
        self.battery = b


    def needs_service(self) -> boolean:
        if e.needs_service() or b.needs_service():
            return True
        return False
