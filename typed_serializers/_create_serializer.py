import inspect
import typing

from . import _serializers

def create_serializer(schema):
    if hasattr(schema, '__load__') and hasattr(schema, '__dump__'):
        return _serializers.SerializerFromClassSchema(schema)


    # `issubclass` won't work on type from the `typing` module
    if hasattr(schema, '__origin__'):
        if schema.__origin__ == list:
            return _serializers.ListSerializer(schema.__args__[0])
        if schema.__origin__ == tuple:
            schemas = [] if schema.__args__ == ((), ) else schema.__args__
            return _serializers.TupleSerializer(schemas)
        if schema.__origin__ == typing.Union:
            return _serializers.UnionSerializer(schema.__args__)


  
    # `None` is a weird special case, and is sometimes replaced by `type(None)`
    if schema is None or schema is type(None):
        return _serializers.NoneSerializer()

    if inspect.isclass(schema):
        if issubclass(schema, bool):
            return _serializers.BoolSerializer()

        if issubclass(schema, float):
            return _serializers.FloatSerializer()

        if issubclass(schema, int):
            return _serializers.IntSerializer()

        if issubclass(schema, str):
            return _serializers.StrSerializer()

    for k in dir(schema):
        print(k, getattr(schema, k))
    # print(schema.__origin__, tuple, type(()), isinstance(schema.__origin__, tuple))
    raise TypeError(schema)
