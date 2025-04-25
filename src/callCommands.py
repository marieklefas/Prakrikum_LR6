from cmd_dir import *
from cmd_file import *


def cmd_help(args, work_dir):
    if not args:
        print('Список команд:')
        for command in allCommands:
            print(f'{command}')
    elif len(args) == 1:
        func = allCommands.get(args[0])
        if func:
            doc = func.__doc__
            print(f'Справка по команде {args[0]}: {doc}')
        else:
            print('Неизвестная команда')
    else:
        print('Неизвестная команда')


allCommands = {
    'help': cmd_help,
    'newdir': cmd_newDir,
    'deldir': cmd_delDir,
    'opendir': cms_openDir,
    'closedir': cmd_closeDir,
    'home': cmd_homeDir,
    'show': cmd_showDir,
    'newfile': cmd_newFile,
    'delfile': cmd_delFile,
    'writefile': cmd_writeFile,
    'readfile': cmd_readFile,
    'copyfile': cmd_copyFile,
    'movefile': cmd_moveFile,
    'renamefile': cmd_renameFile
}


def find_command(command, args, work_dir):
    if command == 'exit':
        return False
    elif command in allCommands:
        allCommands[command](args, work_dir)
    else:
        print('Неизвестная команда')
    return True
