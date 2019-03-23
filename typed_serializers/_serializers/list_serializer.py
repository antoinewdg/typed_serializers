from typing import List, Any, TypeVar
from typed_serializers.errors import ValidationError
from typed_serializers.serializer import Serializer

T = TypeVar('T')


class ListSerializer(Serializer[List[T]]):
    _inner_serializer: Serializer[T]

    def __init__(self, inner_schema):
        # Import needed here to avoid infinite recursion
        from typed_serializers._create_serializer import create_serializer
        self._inner_serializer = create_serializer(inner_schema)

    def load(self, x: Any) -> List[T]:
        if not isinstance(x, (list, tuple)):
            raise ValidationError(f'Expected list, got {x}')

        values = []
        errors = []
        for idx, element in enumerate(x):
            try:
                loaded_elt = self._inner_serializer.load(element)
                values.append(loaded_elt)
            except ValidationError as error:
                errors.append((idx, error.value))

        if errors:
            raise ValidationError(errors)

        return values

    def dump(self, x: List[T]) -> Any:
        return [self._inner_serializer.dump(elt) for elt in x]
