from computer import Computer


class MyComputerBuilder(object):

    def get_computer(self):
        return self._computer

    def build_computer(self):
        self._computer = Computer()
        self.get_case()
        self.build_mainboard()

    def get_case(self):
        self._computer.case = 'CoolerMaster'

    def build_mainboard(self):
        self._computer.mainboard = 'MSI B250'
        self._computer.cpu = 'Intel Core I7 7700'
