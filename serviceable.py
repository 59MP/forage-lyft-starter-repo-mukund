from abc IMPORT abc, abstractmethod

class Serviceable(ABC):

    @abstractmethod
    def needs_service(self) -> boolean:
        pass
