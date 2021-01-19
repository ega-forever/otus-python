from .exceptions.base_car_exceptions import StartEngineError, StopEngineError
from .models import BaseCar
from .models.base_car import EngineProps


class CarMioRio(BaseCar):

    def __init__(self, weight, jack_lift):
        super().__init__(weight, jack_lift)
        self.__engine_running = False

    def check_wheel_pressure(self) -> bool:
        return True

    def beep(self) -> None:
        print("car make beep")

    def clean_up(self) -> None:
        print("the car has been cleaned up")

    def engine_start(self) -> bool:

        if self.__engine_running:
            raise StartEngineError()

        self.__engine_running = True
        return True

    def engine_stop(self) -> bool:

        if self.__engine_running == False:
            raise StopEngineError()

        self.__engine_running = False
        return True

    def get_engine_props(self) -> EngineProps:
        return EngineProps(oil='ai95', capacity=12.9)
