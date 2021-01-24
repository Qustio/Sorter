import huepy
from os.path import join
from sys import exit


def making_dir(path, to_dir):
    run('   Making {} directory'
        .format(huepy.blue(join(path, to_dir)))
        .replace('\\', '/'))


def auto_log(name, from_dir, to_dir):
    run('{} from {} to {}'
        .format(huepy.green(name),
                huepy.blue(from_dir),
                huepy.blue(to_dir))
        .replace('\\', '/'))


def question(text):
    if str(input(huepy.que(text))).lower() == 'y':
        return True
    else:
        return False


def info(text):
    print(huepy.info(text))


def run(text):
    print(huepy.run(text))


def good(text):
    print(huepy.good(text))


def bad(text):
    print(huepy.bad(text))


def end():
    exit()
