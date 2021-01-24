import Message
from os.path import join as join
import os


class Files:

    def __init__(self, name, from_dir):
        self.name = name
        self.format = name.split('.')[-1]
        self.from_dir = from_dir

    def move(self, to_dir, path):
        if not os.path.exists(join(path, to_dir)):
            Message.making_dir(path, to_dir)
            os.makedirs(join(path, to_dir), exist_ok=True)
        Message.auto_log(self.name, self.from_dir, path, to_dir)
        os.replace(self.from_dir, join(path, to_dir, self.name))
        return True
