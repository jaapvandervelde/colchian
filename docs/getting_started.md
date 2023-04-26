## Getting started

There are no requirements or dependencies for the package, but it is assumed you have dictionary-based data structures you want to validate. One easy way to get those is by using the standard library for loading `json`, or third party libraries for loading `.yaml`.

### Installation

You can install Colchian from PyPI using `pip` like this:
```commandline
python -m pip install colchian
```

If you already have Colchian installed and just need the latest version:
```commandline
python -m pip install colchian --upgrade
```

# Example of use

There's a lot of documentation on the [Colchian class](../colchian), and a [large set of examples]((../examples)) to give a more complete overview of what's possible, but here's a simple example to get you started:

``` { .py .copy }
from colchian import Colchian

# Define the structure and types of a valid data dictionary
type_dict = {
    "an integer": int,
    "some strings": [str]
}

# The data to validate
data = {
    "an integer": 42,
    "some strings": ["vastly", "hugely", "mind-bogglingly", "big"]
}

# data that won't validate
not_valid = {
    "an integer": "one"
}

try:
    # Validate/correct the data
    valid_data = Colchian.validated(data, type_dict)
    print(f'Valid:\n{valid_data}')
    # and provide some output that shows what happens when data can't be validated
    Colchian.validated(not_valid, type_dict)
except SyntaxError as e:
    # just print the error message
    print(f'Something is wrong: {e}')
```
Output:
```none
Valid:
{'an integer': 42, 'some strings': ['vastly', 'hugely', 'mind-bogglingly', 'big']}
Something is wrong: strict type mismatch (no casting) at `["an integer"]`, expected `int`, found `str`
```
Note that the error message cannot say that the name of the dictionary is `not_valid`, but does tell you that the problem occurred at `["an integer"]`. There are no line numbers, since `Colchian` validates the dictionary, not whatever source file the dictionary came from. Check the [examples]((../examples)) for suggestions on that.
