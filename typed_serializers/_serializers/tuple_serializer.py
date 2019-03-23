from typing import Tuple, Any, TypeVar, List
from typed_serializers.errors import ValidationError
from typed_serializers.serializer import Serializer

T = TypeVar('T')


class TupleSerializer(Serializer[Tuple]):
    _inner_serializer: List[Serializer]

    def __init__(self, inner_schemas):
        # Import needed here to avoid infinite recursion
        from typed_serializers._create_serializer import create_serializer
        self._inner_serializers = [create_serializer(s) for s in inner_schemas]

    def load(self, x: Any) -> Tuple:
        if not isinstance(x, (list, tuple)):
            raise ValidationError(f'Expected tuple, got {x}')

        expected_len = len(self._inner_serializers)
        if not len(x) == expected_len:
            raise ValidationError(f'Expected {expected_len}-length tuple, got {x}')

        values = []
        errors = []
        for idx, (element, serializer) in enumerate(zip(x, self._inner_serializers)):
            try:
                loaded_elt = serializer.load(element)
                values.append(loaded_elt)
            except ValidationError as error:
                errors.append((idx, error.value))

        if errors:
            raise ValidationError(errors)

        return tuple(values)

    def dump(self, x: Tuple) -> Any:
        expected_len = len(self._inner_serializers)
        if not len(x) == expected_len:
            raise ValueError(f'Expected a {expected_len}-lenght tuple, got {x}')
        return [s.dump(elt) for elt, s in zip(x, self._inner_serializers)]
