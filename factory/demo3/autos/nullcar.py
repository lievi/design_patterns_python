from .abs_auto import AbsAuto


class NullCar(AbsAuto):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def start(self):
        print(f'Unknow car')

    def stop(self):
        pass
