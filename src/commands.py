def cmd_help(args):
    if not args:
        print('Список команд:')
        for command in allCommands:
            print(f'{command}')
    elif len(args) == 1:
        func = allCommands.get(args[0])
        #print(func)
        if func:
            doc = func.__doc__
            print(f'Справка по команде {args[0]}: {doc}')
        else:
            print('Неизвестная команда')
    else:
        print('Неизвестная команда')


def cmd_back(args):
    '''Поднимается на одну директорию выше.'''
    print('sss')



allCommands = {
    'help': cmd_help,
    'back': cmd_back
}