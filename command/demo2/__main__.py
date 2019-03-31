from create_order import CreateOrder
from update_order import UpdateOrder
from no_command import NoCommand
import sys


def get_commands():
    commands = (CreateOrder, UpdateOrder)
    return dict([cls.name, cls] for cls in commands)


def print_usage(commands):
    print('Usage python-m Command CommandName [arguments]')
    print('Commands:')
    for command in commands.values():
        print(f'     {command.description}')


def parse_command(commands, args):
    command = commands.setdefault(args[0], NoCommand)
    return command(args)


commands = get_commands()
if len(sys.argv) < 2:
    print_usage(commands)
    exit()

command = parse_command(commands, sys.argv[1:])
command.execute()
