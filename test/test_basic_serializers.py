import pytest

from typed_serializers import ValidationError, create_serializer
from .test_data import NONE, BOOLS, INTS, FLOATS, STRS, OTHERS


@pytest.mark.parametrize('x', INTS)
def test_int_serializer_valid(x):
    serializer = create_serializer(int)
    assert serializer.load(x) == x
    assert serializer.dump(x) == x


@pytest.mark.parametrize('x', NONE + BOOLS + FLOATS + STRS + OTHERS)
def test_int_serializer_invalid(x):
    serializer = create_serializer(int)
    with pytest.raises(ValidationError):
        serializer.load(x)


def test_none_serializer_valid():
    serializer = create_serializer(None)
    assert serializer.load(None) is None
    assert serializer.dump(None) is None


@pytest.mark.parametrize('x', BOOLS + INTS + FLOATS + STRS + OTHERS)
def test_none_serializer_invalid(x):
    serializer = create_serializer(None)
    with pytest.raises(ValidationError):
        serializer.load(x)


@pytest.mark.parametrize('x', BOOLS)
def test_bool_serializer_valid(x):
    serializer = create_serializer(bool)
    assert serializer.load(x) == x
    assert serializer.dump(x) == x


@pytest.mark.parametrize('x', NONE + INTS + FLOATS + STRS + OTHERS)
def test_bool_serializer_invalid(x):
    serializer = create_serializer(bool)
    with pytest.raises(ValidationError):
        serializer.load(x)


@pytest.mark.parametrize('x', INTS + FLOATS)
def test_float_serializer_valid(x):
    serializer = create_serializer(float)
    assert serializer.load(x) == x
    assert serializer.dump(x) == x


@pytest.mark.parametrize('x', NONE + BOOLS + STRS + OTHERS)
def test_float_serializer_invalid(x):
    serializer = create_serializer(float)
    with pytest.raises(ValidationError):
        serializer.load(x)


@pytest.mark.parametrize('x', STRS)
def test_serializer_str_valid(x):
    serializer = create_serializer(str)
    assert serializer.load(x) == x
    assert serializer.dump(x) == x


@pytest.mark.parametrize('x', NONE + BOOLS + INTS + FLOATS + OTHERS)
def test_serializer_str_invalid(x):
    serializer = create_serializer(str)
    with pytest.raises(ValidationError):
        serializer.load(x)