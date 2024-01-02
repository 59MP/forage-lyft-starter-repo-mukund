from tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tries_wear

    def needs_service(self):
        count = 0
        for t in tire_wear:
            if t >= 0.9:
                count+= 1

        return count >= 1
