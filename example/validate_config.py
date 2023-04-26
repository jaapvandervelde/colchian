from colchian import Colchian
import json
from pathlib import Path


def exists(path, is_dir=False):
    path = Path(path)
    if is_dir:
        if path.is_dir():
            return path
        else:
            raise Exception(f'Path "{path}" is not a directory')
    else:
        if path.is_file():
            return path
        else:
            raise Exception(f'Path "{path}" is not a file')


class MyColchian(Colchian):
    last_keys = None

    @classmethod
    def format_keys(cls, keys):
        cls.last_keys = keys
        return super().format_keys(keys)


try:
    with open('config.json') as f:
        cfg = MyColchian.validated(json.load(f), {
            'path': (exists, True),
            'executable': exists,
            'arguments': [str]
        })
except SyntaxError as e:
    print(f'Error {e}, at {MyColchian.last_keys}')