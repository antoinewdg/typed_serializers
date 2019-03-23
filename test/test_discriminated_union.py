from typing import Union, List, Tuple
from dataclasses import dataclass

import pytest

from typed_serializers import ValidationError, create_serializer
from typed_serializers.schemas import discriminated_union

from .test_data import NONE, BOOLS, INTS, FLOATS, STRS, OTHERS


@dataclass
class Dog:
    name: str
    type: str = 'dog'


@dataclass
class Fish:
    color: int
    type: str = 'fish'


Pet = discriminated_union(Union[Dog, Fish], 'type')


def test_simple_discriminated_union_valid():
    x = {'type': 'dog', 'name': 'Fido'}
    serializer = create_serializer(Pet)
    assert serializer.load(x) == Dog(name='Fido')

    x = {'type': 'fish', 'color': 4}
    serializer = create_serializer(Pet)
    assert serializer.load(x) == Fish(color=4)


@pytest.mark.parametrize('x', [
    {'type': 'dog'},
    {'type': 'dog', 'color': 3},
    {'type': 'fish'},
    {'type': 'fish', 'name': 'FIDO'},
])
def test_simple_discriminated_union_invalid(x):
    serializer = create_serializer(Pet)
    with pytest.raises(ValidationError):
        serializer.load(x)
