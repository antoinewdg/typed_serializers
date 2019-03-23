from typing import Any
from datetime import datetime

from typed_serializers import create_serializer, ValidationError


class DatetimeFromIsoformat(datetime):

    _str_serializer = create_serializer(str)

    @classmethod
    def __load__(cls, x: Any) -> datetime:
        x = cls._str_serializer.load(x)
        try:
            return datetime.fromisoformat(x)
        except ValueError as error:
            raise ValidationError(str(error))

    @classmethod
    def __dump__(cls, x: datetime) -> Any:
        return x.isoformat()