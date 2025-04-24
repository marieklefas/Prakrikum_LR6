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
    if not args:
        file_name = input(
            f'Введите название(я) файла(ов) с расширением: ').split()
    else:
        file_name = args
    for file in file_name:
        if len(file.split('.')) == 2 and all(file.split('.')):
            file_path = f'{work_dir}{globals.cur_dir}/{file}'
            if os.path.exists(file_path):
                print(f'Файл {file} уже существует.')
            else:
                with open(file_path, 'w') as f:
                    pass
                print(f'Файл {file} успешно создан.')
        else:
            print(f'Некорректный ввод файла {file}. Повторите попытку.')


def cmd_delFile(args, work_dir):
    if not args:
        file_name = input(
            f'Введите название(я) файла(ов) с расширением: ').split()
    else:
        file_name = args
    for file in file_name:
        if len(file.split('.')) == 2 and all(file.split('.')):
            file_path = f'{work_dir}{globals.cur_dir}/{file}'
            if os.path.isfile(file_path):
                answer = input(
                    f'Вы уверены, что хотите удалить файл {file}? Данные в нем будут утеряны. [Y/N] ')
                if answer.lower() == 'y':
                    os.remove(file_path)
                    print(f'Файл {file} успешно удален.')
            else:
                print(f'Файлы не найдены.')
        else:
            print(f'Некорректный ввод файла {file}. Повторите попытку.')


def cmd_readFile(args, work_dir):
    if not args:
        file_name = input(
            f'Введите название файла с расширением, который вы хотите прочитать: ').split()
        if len(file_name) > 1:
            print('Введите только один файл.')
            return
        else:
            file = file_name[0]
    elif len(args) > 1:
        print('Введите только один файл.')
        return
    else:
        file = args[0]

    if len(file.split('.')) == 2 and all(file.split('.')):
        file_path = f'{work_dir}{globals.cur_dir}/{file}'
        if not os.path.isfile(file_path):
            print(f'Файл {file} не найден.')
        else:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    print(f'Содержимое файла {file}:')
                    print(content if content else '(файл пуст)')
            except Exception as e:
                print(f'Ошибка при чтении в файл: {e}')
    else:
        print(f'Некорректный ввод файла {file}. Повторите попытку.')


def cmd_writeFile(args, work_dir):
    if not args:
        file_name = input(
            f'Введите название файла с расширением, в который вы хотите записать данные: ').split()
        if len(file_name) > 1:
            print('Введите только один файл.')
            return
        else:
            file = file_name[0]
    elif len(args) > 1:
        print('Введите только один файл.')
        return
    else:
        file = args[0]

    if len(file.split('.')) == 2 and all(file.split('.')):
        file_path = f'{work_dir}{globals.cur_dir}/{file}'
        if not os.path.isfile(file_path):
            print(f'Файл {file} не найден.')
        else:
            print(
                'Введите текст для записи в файл. Чтобы завершить ввод, оставьте строку пустой и нажмите Enter:')
            lines = []
            while True:
                line = input()
                if line == '':
                    break
                lines.append(line)
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(lines))
                print(f'Данные успешно записаны в файл {file}.')
            except Exception as e:
                print(f'Ошибка при записи в файл: {e}')
    else:
        print(f'Некорректный ввод файла {file}. Повторите попытку.')


def cmd_copyFile(args, work_dir):
    if not args:
        file_name = input(
            f'Введите название файла с расширением, который вы хотите скопировать: ').split()
        if len(file_name) > 1:
            print('Введите только один файл.')
            return
        else:
            file = file_name[0]
    elif len(args) > 1:
        print('Введите только один файл.')
        return
    else:
        file = args[0]

    if len(file.split('.')) == 2 and all(file.split('.')):
        file_path = f'{work_dir}{globals.cur_dir}/{file}'
        if not os.path.isfile(file_path):
            print(f'Файл {file} не найден.')
        else:
            dir_name = input(
                f'Введите название папки, в которую вы хотите скопировать файл {file}: ')
            directory = f'{work_dir}{globals.cur_dir}'
            for item in os.listdir(directory):
                new_file_path = os.path.join(directory, item)
                if item == dir_name:
                    new_file_path += f'/{file}'
                    try:
                        shutil.copy2(file_path, new_file_path)
                        print(
                            f'Файл {file} успешно скопирован в папку {dir_name}.')
                        return
                    except Exception as e:
                        print(f'Ошибка при копировании файла: {e}')
                        return
            else:
                print('Такой директории не существует.')
    else:
        print(f'Некорректный ввод файла {file}. Повторите попытку.')


def cmd_moveFile(args, work_dir):
    if not args:
        file_name = input(
            f'Введите название файла с расширением, который вы хотите скопировать: ').split()
        if len(file_name) > 1:
            print('Введите только один файл.')
            return
        else:
            file = file_name[0]
    elif len(args) > 1:
        print('Введите только один файл.')
        return
    else:
        file = args[0]

    if len(file.split('.')) == 2 and all(file.split('.')):
        file_path = f'{work_dir}{globals.cur_dir}/{file}'
        if not os.path.isfile(file_path):
            print(f'Файл {file} не найден.')
        else:
            dir_name = input(
                f'Введите название папки, в которую вы хотите переместить файл {file}: ')
            directory = f'{work_dir}{globals.cur_dir}'
            for item in os.listdir(directory):
                new_file_path = os.path.join(directory, item)
                if item == dir_name:
                    new_file_path += f'/{file}'
                    try:
                        shutil.move(file_path, new_file_path)
                        print(
                            f'Файл {file} успешно перемещен в папку {dir_name}.')
                        return
                    except Exception as e:
                        print(f'Ошибка при копировании файла: {e}')
                        return
            else:
                print('Такой директории не существует.')
    else:
        print(f'Некорректный ввод файла {file}. Повторите попытку.')


def cmd_renameFile(args, work_dir):
    if not args:
        file_name = input(
            f'Введите название файла с расширением, который вы хотите переименовать: ').split()
        if len(file_name) > 1:
            print('Введите только один файл.')
            return
        else:
            file = file_name[0]
    elif len(args) > 1:
        print('Введите только один файл.')
        return
    else:
        file = args[0]

    if len(file.split('.')) == 2 and all(file.split('.')):
        file_path = f'{work_dir}{globals.cur_dir}/{file}'
        if not os.path.isfile(file_path):
            print(f'Файл {file} не найден.')
        else:
            new_file_name = input(f'Введите новое название файла: ').split()
            if len(new_file_name) > 1:
                print('Введите только один название.')
                return
            else:
                new_file = new_file_name[0]
                if len(new_file.split('.')) == 2 and all(new_file.split('.')):
                    new_file_path = f'{work_dir}{globals.cur_dir}/{new_file}'
                    try:
                        os.rename(file_path, new_file_path)
                        print(f'Файл переименован: "{file}" → "{new_file}"')
                    except Exception as e:
                        print(f'Ошибка при переименовании файла: {e}')
                else:
                    print(
                        f'Некорректный ввод файла {new_file}. Повторите попытку.')
    else:
        print(f'Некорректный ввод файла {file}. Повторите попытку.')


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
