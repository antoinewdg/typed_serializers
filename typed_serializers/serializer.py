
from typing import Any, Generic, TypeVar, Union

T = TypeVar('T')

class Serializer(Generic[T]):
    def load(self, x: Any) -> T:
        ...

    def dump(self, x: T) -> Any:
        ...