# Wildcards

An important part of the flexibility and power of Colchian lies in the use of wildcards.

Here's an example of use of different types of wildcards:
```python
from colchian import Colchian

td = {
    str: int,
    int: str,
    'words': {'*:1': str, '*:two': [str]}
}
v = Colchian.validated({
    'start': 1,
    'end': 3,
    4: 'four!',
    'words': {
        '1': 'one',
        2: 'two',
        3: ['three', 'trio']
    }
}, td)
print(v)
```
Running this results in this output:
```none
{'start': 1, 'end': 3, 'words': {'1': 'one', 2: 'two', 3: ['three', 'trio']}}
```
The code above demonstrates the use of the following wildcards:
- `str` as a key with an `int` value in the type dictionary, which means that any key that is not explicitly defined in the type dictionary can be validated as a string, with an integer value;
- `int` as the inverse, so both `str` keys with `int` values and `int` keys with `str` values are allowed. 
- `'*:1'` as a key in the type dictionary, which means that any key here can be validated as a string; `'*:two'` as a second option, which means that any key here can also be validated as a list of strings;
- the data example shows that both `'start': 1` and `'end': 3` are valid, and that all three variants in `words` are valid as well.

Note that adding a key/value pair like `5: 5` would cause a `Colchian.ValidationError` to be thrown.

The three types of wildcards are: types, `'*'`, and `'*:<n/name>'`. Note that using `'*'` or `'*:x'` does not enforce a type, but using a type as a key does.