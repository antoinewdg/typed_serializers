from typing import List

import pytest

from typed_serializers import ValidationError, create_serializer
from .test_data import PRIMITIVES, DICTS


@pytest.mark.parametrize(
    'schema,x', [
        (int, []),
        (float, []),
        (bool, []),
        (int, [1, 4, -123, 1394]),
        (bool, [False, True, False]),
        (List[None], []),
        (List[None], [[None], [], [None, None, None]]),
        (float, (1.0, 4, -193801423.329484)),
    ]
)
def test_list_valid(x, schema):
    serializer = create_serializer(List[schema])
    loaded = serializer.load(x)

    assert serializer.load(x) == [a for a in x]
    assert serializer.dump(loaded) == loaded


@pytest.mark.parametrize('schema', [int, None, float, List[int]])
@pytest.mark.parametrize('x', PRIMITIVES + DICTS)
def test_list_basic_invalid(x, schema):
    serializer = create_serializer(List[schema])
    with pytest.raises(ValidationError):
        serializer.load(x)


@pytest.mark.parametrize('schema,x', [
    (int, [0.4]),
    (bool, [1, 4, -1029, 0]),
])
def test_list_less_basic_invalid(x, schema):
    serializer = create_serializer(List[schema])
    with pytest.raises(ValidationError):
        serializer.load(x)
