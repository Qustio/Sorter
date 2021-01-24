from packages import message
from packages import parser
from packages import files


def main():
    config = parser.read_config()
    path, scan_dir, exceptions = parser.read_settings()
    files_list = files.scanning_files(scan_dir, exceptions)
    message.info("%d files founded" % len(files_list))
    message.run("Moving files:")
    try:
        count = 0
        for file in files_list:
            for (dir, exts) in config.items():
                if file.ext in exts:
                    if file.move(dir, path):
                        count += 1
    except BaseException:
        message.bad("Error while moving files")
        message.end()
    message.info("%d files moved" % count)
    message.good("Done!")
    message.end()


if __name__ == "__main__":
    main()
