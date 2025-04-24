import os
import shutil
import globals


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


def cmd_newDir(args, work_dir):
    if not args:
        dir_name = input(f'Введите название новой папки: ')
    else:
        dir_name = ' '.join(args)
    directory = f'{work_dir}{globals.cur_dir}/{dir_name}'
    if os.path.exists(directory):
        print('Директория уже существует.')
    else:
        os.makedirs(directory)
        print(f'Директория "{dir_name}" создана.')


def cmd_delDir(args, work_dir):
    if not args:
        dir_name = input(f'Введите название папки, которую хотите удалить: ')
    else:
        dir_name = ' '.join(args)
    directory = f'{work_dir}{globals.cur_dir}'
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if item == dir_name:
            answer = input(f'Вы уверены, что хотите удалить эту директорию? Все файлы в ней будут утеряны. [Y/N] ')
            if answer.lower() == 'y':
                directory = f'{work_dir}{globals.cur_dir}/{dir_name}'
                shutil.rmtree(directory)
                print('Директория успешно удалена.')
                return
            else:
                return
    else:
        print('Такой директории не существует, либо вы пытаетесь удалить родительскую директорию.')

def cms_openDir(args, work_dir):
    if not args:
        dir_name = input(f'Введите название папки, которую хотите открыть: ')
    else:
        dir_name = ' '.join(args)
    directory = f'{work_dir}{globals.cur_dir}/{dir_name}'
    if os.path.exists(directory):
        globals.cur_dir += '/' + dir_name
    else:
        print('Такой директории не существует.')


def cmd_closeDir(args, work_dir):
    '''Поднимается в родительскую директорию указанной директории.'''
    if not args:
        globals.cur_dir = globals.cur_dir[:globals.cur_dir.rfind('/')]
    else:
        dir_name = ' '.join(args)
        if dir_name in globals.cur_dir:
            globals.cur_dir = globals.cur_dir[:globals.cur_dir.rfind(
                f'/{dir_name}')]
        else:
            print('Такой директории не существует.')


def cmd_homeDir(args, work_dir):
    globals.cur_dir = ''

def cmd_showDir(args, work_dir):
    directory = f'{work_dir}{globals.cur_dir}'
    if not os.path.isdir(directory):
        print(f'Указанный путь не является директорией.')
        return
    print(f'Содержимое директории:')
    try:
        for item in os.listdir(directory):
            full_path = os.path.join(directory, item)
            if os.path.isdir(full_path):
                print(f'{item}')
            else:
                print(f'      {item}')
    except Exception as e:
        print(f'Ошибка при чтении директории: {e}')

def cmd_newFile(args, work_dir):
    pass

def cmd_delFile(args, work_dir):
    pass

def cmd_readFile(args, work_dir):
    pass

def cmd_writeFile(args, work_dir):
    pass

def cmd_copyFile(args, work_dir):
    pass

def cmd_moveFile(args, work_dir):
    pass

def cmd_renameFile(args, work_dir):
    pass



allCommands = {
    'help': cmd_help,
    'newdir': cmd_newDir,
    'deldir': cmd_delDir,
    'opendir': cms_openDir,
    'closedir': cmd_closeDir,
    'home': cmd_homeDir,
    'show': cmd_showDir
}
