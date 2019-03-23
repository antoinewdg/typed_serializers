from typing import Any, Generic, TypeVar, Type

T = TypeVar('T')

class Serializer(Generic[T]):
    output_class: Type[T]

    def load(self, x: Any) -> T:
        ...

    def dump(self, x: T) -> Any:
        ...
