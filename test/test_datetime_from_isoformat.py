from datetime import datetime
import pytest

from typed_serializers import create_serializer, ValidationError
from typed_serializers.schemas import DatetimeFromIsoformat

from .test_data import NONE, BOOLS, INTS, FLOATS, STRS, OTHERS

@pytest.mark.parametrize('x', ['2014-05-12T00:12:12.453045', '2019-08-12T15:00:12'])
def test_from_isoformat_valid(x):
    serializer = create_serializer(DatetimeFromIsoformat)
    loaded = serializer.load(x)
    assert loaded == datetime.fromisoformat(x)
    assert serializer.dump(loaded) == x


@pytest.mark.parametrize('x', NONE + BOOLS + INTS + FLOATS + STRS + OTHERS)
def test_from_isoformat_invalid(x):
    serializer = create_serializer(DatetimeFromIsoformat)
    with pytest.raises(ValidationError):
        serializer.load(x)
