import sys
from command_executor import CommandExecutor

if len(sys.argv) < 2:
    print("""
Usage: <Command> <Argument>
Commands:
    CreateOrder,
    UpdateQuantity <number>
    ShipOrder
""")
    exit()

executor = CommandExecutor()
executor.execute_command(sys.argv[1:])
