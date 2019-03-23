from . import _serializers

def create_serializer(schema):
    if hasattr(schema, '__load__') and hasattr(schema, '__dump__'):
        return _serializers.SerializerFromClassSchema(schema)


    # `issubclass` won't work on type from the `typing` module
    if hasattr(schema, '__origin__'):
        if issubclass(schema.__origin__, list):
            return _serializers.ListSerializer(schema.__args__[0])


    # `None` is a weird special case, and is sometimes replaced by `type(None)`
    if schema is None or schema is type(None):
        return _serializers.NoneSerializer()

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
    raise TypeError(schema)