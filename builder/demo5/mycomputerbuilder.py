from computer import Computer
from abs_builder import AbsBuilder


class MyComputerBuilder(AbsBuilder):

    def get_case(self):
        self._computer.case = 'CoolerMaster'

    def build_mainboard(self):
        self._computer.mainboard = 'MSI B250'
        self._computer.cpu = 'Intel Core I7 7700'
