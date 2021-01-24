from packages import message
from packages import parser
from packages import files


def main():
    config = parser.read_config()
    path, scan_dir = parser.read_settings()
    files_list = files.scanning_files(scan_dir)
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
