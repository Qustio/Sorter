import message
from os.path import join, isfile
import os


class Files:

    def __init__(self, name, from_dir):
        self.name = name
        self.format = name.split('.')[-1]
        self.from_dir = from_dir

    def move(self, to_dir, path):
        if not os.path.exists(join(path, to_dir)):
            message.making_dir(path, to_dir)
            os.makedirs(join(path, to_dir), exist_ok=True)
        message.auto_log(self.name, self.from_dir, path, to_dir)
        os.replace(self.from_dir, join(path, to_dir, self.name))
        return True


def scanning_files(scan_dir):
    message.run("Scanning directory...")
    exceptions_list = ["desktop.ini"]
    try:
        files_list = []
        for path in scan_dir:
            dir_list = os.listdir(path)
            for (i, file) in enumerate(dir_list):
                if (isfile(join(path, file)) and
                   not (file in exceptions_list)):
                    files_list.append(Files(file, join(path, file)))
        if len(files_list) == 0:
            message.info("No files founded")
            message.end()
        return files_list
    except FileNotFoundError:
        message.bad("Directory not founded")
        message.end()
