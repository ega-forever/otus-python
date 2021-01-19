from abc import ABC, abstractmethod
from attr import dataclass
from homework2.models.base_vehicle import BaseVehicle

@dataclass
class EngineProps:
    oil: str
    capacity: float


class BaseCar(BaseVehicle, ABC):

    @abstractmethod
    def check_wheel_pressure(self) -> bool:
        pass

    @abstractmethod
    def get_engine_props(self) -> EngineProps:
        pass