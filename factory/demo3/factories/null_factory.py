from .abs_factory import AbsFactory
from autos.nullcar import NullCar


class ChevyFactory(AbsFactory):
    def create_auto(self):
        self.null = null_car = NullCar()
        self.null.name = 'Null Car'
        return self.null
