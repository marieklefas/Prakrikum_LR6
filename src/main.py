import configparser
from callCommands import find_command
import globals


def load_config():
    config = configparser.ConfigParser()
    config.read('config\config.ini')
    return config['DEFAULT']['workdir']


def main():
    work_dir = load_config()
    print('user: ', work_dir)

    print("Добро пожаловать в файловый менеджер. Введите 'help' для списка команд.")

    while True:
        command = input(f'user{globals.cur_dir}: ').split()
        if not command:
            continue

        command, args = command[0], command[1:]

        if not find_command(command, args, work_dir):
            break


if __name__ == "__main__":
    main()
