import os
import shutil
import globals


def cmd_newFile(args, work_dir):
    '''Создание новго файла в текущей директории. Необходимо ввести название файла с расширением в формате name.txt'''
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
    '''Удаление файла. Необходимо ввести название файла с расширением в формате name.txt'''
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
    '''Чтение файла в текущей директории. Необходимо ввести название файла с расширением в формате name.txt'''
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
    '''Запись новых данных в существующий файл. Необходимо ввести название файла с расширением в формате name.txt А далее вводить сами данные.'''
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
    '''Копирование файла из текущей директории в другую. Необходимо ввести название файла с расширением в формате name.txt'''
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
    '''Перемещение файла из текущей директории в дочернюю. Необходимо ввести название файла с расширением в формате name.txt'''
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
    '''Переименовать файл. Необходимо ввести название файла с расширением в формате name.txt'''
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
