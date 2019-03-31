from command_abc import AbsCommand
from order_command_abc import AbsOrderCommand


class NoCommand(AbsCommand, AbsOrderCommand):
    name = 'NoCommand'
    description = 'NoCommand'

    def __init__(self, args):
        self._command = args[0]

    def execute(self):
        print(f'No command named {self._command}')
