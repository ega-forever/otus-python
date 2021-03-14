from abc import ABC, abstractmethod
from attr import dataclass
from homework2.models.base_vehicle import BaseVehicle

@dataclass
class WingsProps:
    length: int
    pressure_max_limit: float

class BasePlane(BaseVehicle, ABC):

    @abstractmethod
    def check_wings_high_pressure(self) -> bool:
        pass

    @abstractmethod
    def check_wings_low_pressure(self) -> bool:
        pass

    @abstractmethod
    def get_wings_props(self) -> WingsProps:
        pass
