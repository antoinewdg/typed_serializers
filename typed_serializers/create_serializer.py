from .basic_serializers import (
    NoneSerializer, BoolSerializer, IntSerializer, FloatSerializer, StrSerializer
)


def create_serializer(schema):
    if schema is None:
        return NoneSerializer()

    if issubclass(schema, bool):
        return BoolSerializer()

    if issubclass(schema, float):
        return FloatSerializer()

    if issubclass(schema, int):
        return IntSerializer()

    if issubclass(schema, str):
        return StrSerializer()

    raise TypeError(schema)
