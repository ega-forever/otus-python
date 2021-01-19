from .models import BasePlane
from .models.base_plane import WingsProps


class PlaneAirBus(BasePlane):

    def check_wings_high_pressure(self) -> bool:
        return True

    def check_wings_low_pressure(self) -> bool:
        return True

    def beep(self) -> None:
        print("plane makes beep")

    def clean_up(self) -> None:
        print("cleaned up plane")

    def engine_start(self) -> bool:
        return True

    def engine_stop(self) -> bool:
        return True

    def get_wings_props(self) -> WingsProps:
        return WingsProps(length=20, pressure_max_limit=12.8)
