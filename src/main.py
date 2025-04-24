import configparser


def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['Settings']['workdir']

def main():
    work_dir = load_config()
        

if __name__ == "__main__":
    main()
