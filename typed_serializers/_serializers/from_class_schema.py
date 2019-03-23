from typing import TypeVar, Type, Any
from typed_serializers.serializer import Serializer

T = TypeVar('T')

class SerializerFromClassSchema(Serializer[T]):
    _schema: Any

    def __init__(self, schema: Type[T]) -> None:
        self._schema = schema

    def load(self, x: Any) -> T:
        return self._schema.__load__(x)

    def dump(self, x: T) -> Any:
        return self._schema.__dump__(x)
