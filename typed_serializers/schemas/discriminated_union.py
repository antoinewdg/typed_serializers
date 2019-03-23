from typing import TypeVar, Type, Any, TYPE_CHECKING

from typed_serializers.errors import ValidationError

U = TypeVar('U')


def discriminated_union(union_type: Type[U], type_key: str) -> Type[U]:
    if TYPE_CHECKING:
        return union_type

    from typed_serializers._create_serializer import create_serializer
    serializers = {getattr(cls, type_key): create_serializer(cls) for cls in union_type.__args__}

    class DiscriminatedUnionSchema:
        @classmethod
        def __load__(cls, x: Any) -> U:
            if not isinstance(x, dict):
                raise ValidationError(f'Expected dict, got {x}')
            try:
                type_ = x[type_key]
            except KeyError:
                raise ValidationError({type_key: 'required'})

            if type_ not in serializers:
                msg = 'Expected on of {}, got {}'
                msg = msg.format(','.join((str(k) for k in serializers)), type_)
                raise ValidationError({type_key: msg})

            serializer = serializers[type_]

            return serializer.load(x)

        @classmethod
        def __dump__(cls, x: U) -> Any:
            type_ = getattr(x, type_key)
            serializer = serializers[type_]
            return serializer.dump(x)

    return DiscriminatedUnionSchema
