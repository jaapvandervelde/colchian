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
