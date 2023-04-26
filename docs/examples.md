## Data types in `Colchian.validated()` results

Consider this:
``` { .py .copy }
from colchian import Colchian


class SquareList(list):
    def __getitem__(self, item):
        return super().__getitem__(item)**2


class EvenDict(dict):
    def __setitem__(self, item, x):
        if x % 2 != 0:
            raise ValueError('Only even numbers allowed')
        return super().__setitem__(item, x)


td = {
    'numbers': [int],
    'shouts': SquareList,
    'evens': EvenDict
}
v = Colchian.validated({
    'numbers': [1, 2, 3],
    'shouts': SquareList([2, 3, 4]),
    'evens': EvenDict({'a': 2, 'b': 8})
}, td)

print(type(v['shouts']), v['shouts'][1])  # show that this is of type SquareList, and "9"
print(type(v['evens']), v['evens'])  # show that this is of type EvenDict, and "{'a': 2, 'b': 8}"
```
This example demonstrates a few points:

- you can use any type as a value in the type dictionary;
- the `.validated()` method will return a new instance of the same type and with the same value as the original;
- this is recursively true for values nested inside the data structure (inside list or dictionary descendents)

## Using Colchian to validate .json files

If you have this configuration file `config.json` (assuming you're on Windows and these locations exist):
``` { .json .copy }
{
  "path": "C:\\Windows\\Temp",
  "executable": "C:\\Windows\\notepad.exe",
  "arguments": ["-a", "b" ,"c", "--fast"]
}
```
The following code will load and validate it:
``` { .py .copy }
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


with open('config.json') as f:
    cfg = Colchian.validated(json.load(f), {
        'path': (exists, True),
        'executable': exists,
        'arguments': [str]
    })

print(cfg)
```
This example demonstrates the following:

- you can use custom validation functions in the type dictionary.
- you can pass additional parameters to those functions, by passing the function and the added arguments in a tuple.
- the validation function can return a different type than the original value (here it returns a `Path` object).

However, if there's a problem with he configuration file, you can't tell what line the problem is on:
``` { .json .copy }
{
  "path": "C:\\Windows\\Temp",
  "executable": "C:\\Path\\to\\non-existing\\file.exe",
  "arguments": ["-a", "b" ,"c", "--fast"]
}
```
Running the script with this config will give you this error:
```none
Colchian.ValidationError: value at `["executable"]` passed to `exists` raised `Path "C:\Path\to\non-existing\file.exe" is not a file`
```
For such a small configuration file, that's fine. But what if this was hidden in a large and complex configuration file?

Colchian doesn't solve that problem by itself, but one approach would be to override the `format_keys()` method of the `Colchian` class, to capture the last set of keys that were formatted, and using those with a third party package like `json_source_map`. 
``` { .py .copy }
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
except Colchian.ValidationError as e:
    print(f'Error {e}, at {MyColchian.last_keys}')
```
The value of `MyColchian.last_keys` could be used with something like `json_source_map` to get the line number of the error.

## Validating more complex structures

Configuration files can typically have many settings, many of which are optional, or structured themselves.

Here's an example of a more complex structure defined using `Colchian`:
``` { .py .copy }
from colchian import Colchian
from pathlib import Path

class MyColchian(Colchian):
    @classmethod
    def existing_path(cls, x, is_file=False, keys=None):
        if (is_file and Path(x).is_file()) or (not is_file and Path(x).is_dir()):
            return x
        else:
            raise Colchian.ValidationError(f'Expected an existing path, got {x}, at {cls.format_keys(keys)}')

    @classmethod
    def data_pair(cls, x, keys=None):
        cls.validated(x, [str])  # validate that x is a list of str, or raise appropriate exception
        if len(x) == 2:
            return x
        else:
            raise Colchian.ValidationError(f'Expected an event, duration pair, '
                                           f'got {x} ({len(x)} elements), at {cls.format_keys(keys)}')


heh_config = {
    "wbnm_run_folder": MyColchian.existing_path,
    "charts_folder": MyColchian.existing_path,
    "data_folder": MyColchian.existing_path,
    "cache_folder": (MyColchian.existing_path, None),
    "overrides": ((MyColchian.existing_path, True), None),
    "executables": {
        "wbnm": (MyColchian.existing_path, True),
        "convert_to_ts1": (MyColchian.existing_path, True)
    },
    "events_durations": [MyColchian.data_pair],
    "models": {
        "*": {
            ("type_1", "type_2"): str,
            "updates": (dict, None),
            "parts": {
                "file": (MyColchian.existing_path, True),
                "component": str,
                "optional": (str, None)
            },
            "data_csv": {
                "folder": MyColchian.existing_path,
                "*": {  # columns 
                    "*": str
                }
            }
        }
    }
}
```
This example shows the following:

- how to add optional elements (by defining the value as a tuple of a type and `None`).
- how to define parts of configuration with very loose configuration (here the `"data_csv"` section only defines a `"folder"` as a required existing path, and the rest of the element is defined as keys with single level dictionaries of strings).
- how to define key name alternatives (`("type_1", "type_2")`).
- how to use the `keys` to provide feedback on the location of the error, in `.data_pair()`.
