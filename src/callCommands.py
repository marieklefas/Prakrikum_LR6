from commands import *


def find_command(command, args, work_dir):
    if command == 'exit':
        return False
    elif command in allCommands:
        allCommands[command](args, work_dir)
    else:
        print('Неизвестная команда')
    return True
