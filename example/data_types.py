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
