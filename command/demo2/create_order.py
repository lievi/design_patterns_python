from command_abc import AbsCommand
from order_command_abc import AbsOrderCommand


class CreateOrder(AbsCommand, AbsOrderCommand):
    name = 'CreateOrder'
    description = 'CreateOrder'

    def __init__(self, args):
        pass

    def execute(self):
        pass
