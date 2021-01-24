import json
from . import message


def read_config():
    message.run("Reading configuration")
    config_name = "config.json"
    try:
        with open(config_name, "r") as read_file:
            config = json.load(read_file)
        return config
    except FileNotFoundError:
        message.info("Config not found")
        if message.question("Create default config file? (y/n): "):
            with open(config_name, "x") as write_file:
                json.dump({
                            "Images": ["png", "jpg", "JPG"],
                            "Music": ["mp3"],
                            "Text": ["txt"]
                          },
                          write_file,
                          indent=4)
        message.end()
    except json.decoder.JSONDecodeError:
        message.bad("Error in config file")
        message.end()


def read_settings():
    message.run("Reading settings")
    settings_name = "settings.json"
    try:
        with open(settings_name, "r") as read_file:
            settings = json.load(read_file)
        path = scrap(settings, "Path")
        scan_dir = scrap(settings, "Scanning directories")
        exceptions = scrap(settings, "Exceptions")
        return path, scan_dir, exceptions
    except FileNotFoundError:
        message.info("Config not found")
        if message.question("Create default settings file? (y/n): "):
            with open(settings_name, "x") as write_file:
                json.dump({
                            "Path": "D:\\Desktop\\Sorted files",
                            "Scanning directories": [
                                "D:\\Desktop",
                            ]
                          },
                          write_file,
                          indent=4)
        message.end()
    except json.decoder.JSONDecodeError:
        message.bad("Error in settings file")
        message.end()


def scrap(dic, name):
    try:
        scrap = dic[name]
        return scrap
    except KeyError:
        message.bad(f"{name} is missing in settings file")
