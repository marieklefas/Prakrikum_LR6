import os
import shutil
import globals


def cmd_newDir(args, work_dir):
    '''Создание новой директории. Требуется ввести название папки либо сразу с командой либо позже.'''
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
    '''Удаление существующей директории. Необходимо ввести название папки.'''
    if not args:
        dir_name = input(f'Введите название папки, которую хотите удалить: ')
    else:
        dir_name = ' '.join(args)
    directory = f'{work_dir}{globals.cur_dir}'
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if item == dir_name:
            answer = input(
                f'Вы уверены, что хотите удалить эту директорию? Все файлы в ней будут утеряны. [Y/N] ')
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
    '''Переход в дочернюю директорию. Необходимо ввести название директории или путь в формате dir1/dir2'''
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
    '''Переход из дочерней директории в родительскую. Можно подняться на одну директорию выше или, указав путь, подняться на несколько директорий выше.'''
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
    '''Возвращение в корневую директорию.'''
    globals.cur_dir = ''


def cmd_showDir(args, work_dir):
    '''Демонстрация всех папко и файлов в директории. Принимает на вход название директории.'''
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
