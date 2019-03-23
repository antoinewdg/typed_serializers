from typing import Union, List, Tuple

import pytest

from typed_serializers import ValidationError, create_serializer
from .test_data import NONE, BOOLS, INTS, FLOATS, STRS, OTHERS


@pytest.mark.parametrize('x', INTS + BOOLS)
def test_int_bool_valid(x):
    serializer = create_serializer(Union[int, bool])
    assert serializer.load(x) == x


@pytest.mark.parametrize('x', NONE + FLOATS + STRS + OTHERS)
def test_int_bool_invalid(x):
    serializer = create_serializer(Union[int, bool])
    with pytest.raises(ValidationError):
        serializer.load(x)


@pytest.mark.parametrize('x', [[], [4, 5], [5, 5, 3, 5], (0.4, 13229), (), (4, 5, 5)])
def test_list_int_tuple_float_valid(x):
    serializer = create_serializer(Union[List[int], Tuple[float, float]])
    assert list(serializer.load(x)) == [a for a in x]


@pytest.mark.parametrize('x', [(1.3), ['a', 'v'], (None, False)])
def test_list_int_tuple_float_invalid(x):
    serializer = create_serializer(Union[List[int], Tuple[float, float]])
    with pytest.raises(ValidationError):
        serializer.load(x)
