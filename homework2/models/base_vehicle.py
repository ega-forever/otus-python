from abc import abstractmethod, ABCMeta


class BaseVehicle(metaclass=ABCMeta):
    def __init__(self, weight, jack_lift):
        self.weight = weight
        self.jack_lift = jack_lift

    @abstractmethod
    def beep(self) -> None:
        pass

    @abstractmethod
    def clean_up(self) -> None:
        pass

    @abstractmethod
    def engine_start(self) -> bool:
        pass

    @abstractmethod
    def engine_stop(self) -> bool:
        pass
