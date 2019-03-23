from typing import Any, TypeVar, Type, Dict, get_type_hints, cast
from typed_serializers.errors import ValidationError
from typed_serializers.serializer import Serializer

T = TypeVar('T')


class ClassSerializer(Serializer[T]):
    _serializers: Dict[str, Serializer[Any]]
    _class: Type[T]

    def __init__(self, class_, serializers):
        self._class = class_
        self._serializers = serializers

    @staticmethod
    def from_class(class_):
        # Import needed here to avoid infinite recursion
        from typed_serializers._create_serializer import create_serializer

        annotations = get_type_hints(class_)
        # import pprint
        # pprint.pprint(annotations)
        serializers = {k: create_serializer(v) for k, v in annotations.items()}
        return ClassSerializer(class_, serializers)

    def load(self, x: Any) -> T:
        if not isinstance(x, dict):
            raise ValidationError(f'Expected dict, got {x}')

        errors = {}
        values = {}
        for key, serializer in self._serializers.items():
            if key not in x:
                errors[key] = 'Required'
                continue
            element = x[key]
            try:
                values[key] = serializer.load(element)
            except ValidationError as error:
                errors[key] = error.value

        if errors:
            raise ValidationError(errors)

        return cast(Any, self._class)(**values)

    def dump(self, x: T) -> Any:
        result = {}
        for key, serializer in self._serializers.items():
            result[key] = serializer.dump(getattr(x, key))

        return result
