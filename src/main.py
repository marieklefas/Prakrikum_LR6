import configparser
import os
from callCommands import find_command

def load_config():
    config = configparser.ConfigParser()
    config.read('config\config.ini')
    return config['DEFAULT']['workdir']


def main():
    work_dir = load_config()
    print('user: ', work_dir)
    print(os.path.abspath(work_dir))

    print("Добро пожаловать в файловый менеджер. Введите 'help' для списка команд.")

    while True:
        command = input('user: ').split()
        if not command:
            continue

        command, args = command[0], command[1:]

        if not find_command(command, args):
            break


if __name__ == "__main__":
    main()
