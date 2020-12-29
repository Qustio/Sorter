import os
import json
import codecs
from os.path import join as join
import huepy
from time import sleep


class Files:

    def __init__(self, name, from_dir):
        self.name = name
        self.format = name.split('.')[-1]
        self.from_dir = from_dir

    def move(self, to_dir, path, auto_mode):
        if not auto_mode:
            if not Message.ask_for_move(self.name,
                                        self.from_dir,
                                        to_dir, path):
                return False
        if not os.path.exists(join(path, to_dir)):
            Message.making_dir(path, to_dir)
            os.makedirs(join(path, to_dir), exist_ok=True)
        if auto_mode:
            Message.auto_log(self.name, self.from_dir, path, to_dir)
        os.replace(self.from_dir, join(path, to_dir, self.name))
        return True


class Message:

    def ask_for_move(name, from_dir, to_dir, path):
        return Message.question('Move {} from {} to {} (y/n)? '
                                .format(huepy.green(name),
                                        huepy.blue(from_dir),
                                        huepy.blue(join(path, to_dir)))
                                .replace('\\', '/'))

    def making_dir(path, to_dir):
        Message.run('   Making {} directory'
                    .format(huepy.blue(join(path, to_dir)))
                    .replace('\\', '/'))

    def auto_log(name, from_dir, path, to_dir):
        Message.run('{} from {} to {}'
                    .format(huepy.green(name),
                            huepy.blue(from_dir),
                            huepy.blue(join(path, to_dir)))
                    .replace('\\', '/'))

    def question(text):
        if str(input(huepy.que(text))).lower() == 'y':
            return True
        else:
            return False

    def info(text):
        print(huepy.info(text))
        sleep(0.5)

    def run(text):
        print(huepy.run(text))
        sleep(0.5)

    def good(text):
        print(huepy.good(text))
        sleep(0.5)

    def bad(text):
        print(huepy.bad(text))
        sleep(0.5)


def quity():
    print()
    input('Press ENTER to close... ')
    quit()


def read_config():
    Message.run('Reading configuration')
    config_name = 'config.json'
    try:
        with codecs.open(config_name, "r", "utf_8_sig") as read_file:
            config = json.load(read_file)
        return config
    except FileNotFoundError:
        Message.info('Config not found')
        if Message.question('Create default config file? (y/n): '):
            with codecs.open(config_name, "x", "utf_8_sig") as write_file:
                json.dump({
                            'Images': ['png', 'jpg', 'JPG'],
                            'Music': ['mp3']
                          },
                          write_file,
                          indent=4)
        quity()
    except json.decoder.JSONDecodeError:
        Message.bad('Error in config file')
        quity()


def read_settings():
    Message.run('Reading settings')
    sleep(0.5)
    settings_name = 'settings.json'
    try:
        with codecs.open(settings_name, "r", "utf_8_sig") as read_file:
            settings = json.load(read_file)
        path = scrap_settings(settings, 'Path')
        scan_dir = scrap_settings(settings, 'Scanning directories')
        auto_mode = scrap_settings(settings, 'Auto mode')
        return path, scan_dir, auto_mode
    except FileNotFoundError:
        Message.info('Config not found')
        sleep(0.5)
        if Message.question('Create default settings file? (y/n): '):
            with codecs.open(settings_name, "x", "utf_8_sig") as write_file:
                json.dump({
                            "Auto mode": False,
                            'Path': 'D:\\',
                            'Scanning directories': [
                                'D:\\', 'D:\\Downloads'
                            ]
                          },
                          write_file,
                          indent=4)
        quity()
    except json.decoder.JSONDecodeError:
        Message.bad('Error in settings file')
        quity()


def scrap_settings(dic, name):
    try:
        scrap = dic[name]
        return scrap
    except KeyError:
        Message.bad(f'{name} is missing in settings file')


def scanning_files(scan_dir):
    Message.run('Scanning directory...')
    exceptions_list = ['desktop.ini']
    try:
        files_list = []
        for path in scan_dir:
            dir_list = os.listdir(path)
            for (i, file) in enumerate(dir_list):
                if (os.path.isfile(join(path, file)) and
                   not (file in exceptions_list)):
                    files_list.append(Files(file, join(path, file)))
        if len(files_list) == 0:
            Message.info('No files founded')
            quity()
        return files_list
    except FileNotFoundError:
        Message.bad('Directory not founded')
        quity()


def main():
    config = read_config()
    path, scan_dir, auto_mode = read_settings()
    files_list = scanning_files(scan_dir)
    Message.info('%d files founded' % len(files_list))
    Message.run('Moving files:')
    try:
        count = 0
        for file in files_list:
            for (dic, formats) in config.items():
                if file.format in formats:
                    if file.move(dic, path, auto_mode):
                        count += 1
    except BaseException:
        Message.bad('Error while moving files')
        quity()
    Message.info('%d files moved' % count)
    Message.good('My work is done!')
    quity()


if __name__ == '__main__':
    main()
