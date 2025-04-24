from commands import *

def find_command(command, args):
    if command == 'exit':
        return False
    elif command in allCommands:
        allCommands[command](args)
    else:
        print('Неизвестная команда')
    return True