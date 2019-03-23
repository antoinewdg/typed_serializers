from typing import Union, Any, List
from typed_serializers.errors import ValidationError
from typed_serializers.serializer import Serializer


class UnionSerializer(Serializer[Union[Any]]):
    _inner_serializers: List[Serializer]

    def __init__(self, inner_schemas):
        # Import needed here to avoid infinite recursion
        from typed_serializers._create_serializer import create_serializer
        self._inner_serializers = [create_serializer(s) for s in inner_schemas]

    def load(self, x: Any) -> Union[Any]:
        errors = []
        for serializer in self._inner_serializers:
            try:
                return serializer.load(x)
            except ValidationError as error:
                errors.append(error)

        raise ValidationError(errors)

    def dump(self, x: Union[Any]) -> Any:
        raise NotImplementedError()
