from computer import Computer
from mycomputerbuilder import MyComputerBuilder

builder = MyComputerBuilder()
builder.build_computer()
computer = builder.get_computer()
computer.display()
