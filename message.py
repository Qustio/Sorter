import huepy
import time
from os.path import join as join


def making_dir(path, to_dir):
    run('   Making {} directory'
        .format(huepy.blue(join(path, to_dir)))
        .replace('\\', '/'))


def auto_log(name, from_dir, path, to_dir):
    run('{} from {} to {}'
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
    time.sleep(0.5)


def run(text):
    print(huepy.run(text))
    time.sleep(0.5)


def good(text):
    print(huepy.good(text))
    time.sleep(0.5)


def bad(text):
    print(huepy.bad(text))
    time.sleep(0.5)


def end():
    input()
    quit()
