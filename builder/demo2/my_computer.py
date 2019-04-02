from computer import Computer


class MyComputer(object):

    def get_computer(self):
        return self._computer

    def build_computer(self):
        computer = self._computer = Computer()
        computer.case = 'CoolerMaster'
        computer.mainboard = 'MSI B250M'
        computer.cpu = 'Intel Core I7 7700'
        computer.memory = 'Hyperx Savage 16GB'
        computer.hard_drive = 'Seagate 1T'
        computer.video_card = 'Geforce GTX 1080'
