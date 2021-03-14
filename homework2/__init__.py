from homework2.car_mio_rio import CarMioRio
from homework2.exceptions.base_car_exceptions import StartEngineError
from homework2.plane_airbus import PlaneAirBus

if __name__ == '__main__':
    mioCar = CarMioRio(12, 1)
    print(f'is car pressure ok: {mioCar.check_wheel_pressure()}')
    mioCar.beep()

    print(f'car engine started: {mioCar.engine_start()}')

    try:
        mioCar.engine_start()
    except (StartEngineError):
        print('car engine can`t be started twice')

    airbusPlane = PlaneAirBus(12, 1)
    print(f'is plane high pressure ok: {airbusPlane.check_wings_high_pressure()}')
    print(f'is plane low pressure ok: {airbusPlane.check_wings_low_pressure()}')
    airbusPlane.beep()
    print(f'airbus wings length {airbusPlane.get_wings_props().length}')





