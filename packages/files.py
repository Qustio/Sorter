from . import message
from os.path import join, isfile, exists
from os import replace, makedirs, listdir


class Files:

    def __init__(self, name, from_dir):
        self.name = name
        self.ext = ext(name)
        self.from_dir = from_dir

    def move(self, to_dir, path):
        if not exists(join(path, to_dir)):
            message.making_dir(path, to_dir)
            makedirs(join(path, to_dir), exist_ok=True)
        message.auto_log(self.name, self.from_dir, path, to_dir)
        replace(self.from_dir, join(path, to_dir, self.name))
        return True


def ext(name):
    return name.split('.')[-1]


def scanning_files(scan_dir, exception_list):
    message.run("Scanning directory")
    try:
        file_list = []
        for path in scan_dir:
            dir_list = listdir(path)
            for obj in dir_list:
                if (isfile(join(path, obj)) and
                        not ext(obj) in exception_list):
                    file_list.append(Files(obj, join(path, obj)))
        if len(file_list) == 0:
            message.info("No files founded")
            message.end()
        return file_list
    except FileNotFoundError:
        message.bad("Directory not founded")
        message.end()
