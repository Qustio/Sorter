import os
import message
import parser
from os.path import join as join
from files import Files


def scanning_files(scan_dir):
    message.run("Scanning directory...")
    exceptions_list = ["desktop.ini"]
    try:
        files_list = []
        for path in scan_dir:
            dir_list = os.listdir(path)
            for (i, file) in enumerate(dir_list):
                if (os.path.isfile(join(path, file)) and
                   not (file in exceptions_list)):
                    files_list.append(Files(file, join(path, file)))
        if len(files_list) == 0:
            message.info("No files founded")
            message.end()
        return files_list
    except FileNotFoundError:
        message.bad("Directory not founded")
        message.end()


def main():
    config = parser.read_config()
    path, scan_dir = parser.read_settings()
    files_list = scanning_files(scan_dir)
    message.info("%d files founded" % len(files_list))
    message.run("Moving files:")
    try:
        count = 0
        for file in files_list:
            for (dic, formats) in config.items():
                if file.format in formats:
                    if file.move(dic, path):
                        count += 1
    except BaseException:
        message.bad("Error while moving files")
        message.end()
    message.info("%d files moved" % count)
    message.good("My work is done!")
    message.end()


if __name__ == "__main__":
    main()
