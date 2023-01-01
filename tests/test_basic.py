import itertools
from pprint import pprint

import pytest

def test_map():
    data = [[1, 3, 4, 4, 1], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
    print(data)
    # [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

    data = map(set, data)
    pprint(list(data))

    data = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
    pprint(list(data))

def test_chain():
    itertools.chain(*map(lambda x: x ** 2, [1, 2, 3, 4, 5]))

def test_max():
    strs = 'hhhdadamdaaaaaaaaak8888'
    max_item = max(strs, key=strs.count)
    print(max_item)