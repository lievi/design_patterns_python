from chevyvolt import ChevyVolt
from fordfocus import FordFocus
from jeepsahara import JeepSahara
from nullcar import NullCar


def get_car(carname):
    if carname == 'Chevy':
        return ChevyVolt()
    elif carname == 'Ford':
        return FordFocus()
    elif carname == 'Jeep':
        return JeepSahara()
    else:
        return NullCar(carname)


for carname in ['Chevy', 'Ford', 'Jeep', 'Tesla']:
    car = get_car(carname)
    car.start()
    car.stop()
