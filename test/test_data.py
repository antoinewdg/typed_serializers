from typing import List, Any

NONE: List[Any] = [None]
BOOLS: List[Any] = [False, True]
INTS: List[Any] = [1, 4, -1, 428, 0, 429483208, -1828842329821]
FLOATS: List[Any] = [1.0, -0.0, -1242.453294392]
STRS: List[Any] = ['toto', '', 'asidjf&$*ufda', '1']
PRIMITIVES: List[Any] = NONE + BOOLS + INTS + FLOATS + STRS

LISTS: List[Any] = [[], [1, 4, -12, 1234], [None, None, 0.4, 1]]
DICTS: List[Any] = [{}, {1: 'one'}, {'a': 1, 'b': 4}]
OTHERS: List[Any] = LISTS + DICTS
