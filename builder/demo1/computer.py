class Computer(object):
    def __init__(self, case, mainboard, cpu, memory, hard_drive, video_card):
        self.case = case
        self.mainboard = mainboard
        self.cpu = cpu
        self.memory = memory
        self.hard_drive = hard_drive
        self.video_card = video_card

    def display(self):
        print(f"""
Custom computer:
Case: {self.case}
MainBoard: {self.mainboard}...
""")
