from dataclasses import dataclass

import pytest

from typed_serializers import create_serializer, ValidationError


@dataclass
class Person:
    name: str
    age: int


def test_person_valid():
    x = {'name': 'toto', 'age': 45}
    expected = Person(name='toto', age=45)
    serializer = create_serializer(Person)
    assert serializer.load(x) == expected
    assert serializer.dump(expected) == x

@pytest.mark.parametrize('x', [
    {'name': 'toto'},
    {'age': 45},
    {'name': 43, 'age': 45},
    {'name': 'toto', 'age': 45.2},
])
def test_person_invalid(x):
    serializer = create_serializer(Person)
    with pytest.raises(ValidationError):
        serializer.load(x)
