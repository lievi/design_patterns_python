class NullCar(object):
    def __init__(self, carname):
        self._carname = carname

    def start(self):
        print(f'Unknow car {self._carname}')

    def stop(self):
        pass
