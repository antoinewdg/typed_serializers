from typing import Tuple

import pytest

from typed_serializers import ValidationError, create_serializer
from .test_data import PRIMITIVES, DICTS

@pytest.mark.parametrize('schema,x', [
    (Tuple[()], []), 
    (Tuple[()], ()), 
    (Tuple[int], (1,)),
    (Tuple[float, str], (1,'toto')),
    (Tuple[float, str, int], (1,'toto', 4)),
])
def test_list_valid(x, schema):
    serializer = create_serializer(schema)
    loaded = serializer.load(x)

    assert serializer.load(x) == tuple([a for a in x])
    assert serializer.dump(loaded) == [a for a in x]

@pytest.mark.parametrize('schema', [Tuple[()], Tuple[None], Tuple[int, float, str]])
@pytest.mark.parametrize('x', PRIMITIVES + DICTS)
def test_tuple_basic_invalid(x, schema):
    serializer = create_serializer(schema)
    with pytest.raises(ValidationError):
        serializer.load(x)
