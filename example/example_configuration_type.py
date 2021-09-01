from typing import Optional, Any
from pathlib import Path
from colchian import Colchian


class MyColchian(Colchian):
    @classmethod
    def existing_path(cls, x, is_file=False, strict=False, keys=None):
        if (is_file and Path(x).is_file()) or (not is_file and Path(x).is_dir()):
            return x
        else:
            raise SyntaxError(f'Expected a existing path, got {x}, at {cls.format_keys(keys)}')


example_configuration_type = {
    'working directory': MyColchian.existing_path,
    'files': str,
    'users': [str],
    'admin': (None, bool),
    "*": {
        'executable': (MyColchian.existing_path, True),
        'arguments': (
            [str],
            {
                '*': Any
            }
        ),
        'wait': Optional[bool],
    }
}
