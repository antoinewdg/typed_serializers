from .serializer import Serializer
from .errors import ValidationError


class NoneSerializer(Serializer[None]):
    def load(self, x):
        if not x is None:
            raise ValidationError(f"Expected None, got {x}")
        return x

    def dump(self, x):
        return x


class BoolSerializer(Serializer[bool]):
    def load(self, x):
        if not isinstance(x, bool):
            raise ValidationError(f'Expected bool, got {x}')
        return x

    def dump(self, x):
        return x


class IntSerializer(Serializer[int]):
    def load(self, x):
        if isinstance(x, bool) or not isinstance(x, int):
            raise ValidationError(f'Expected int, got {x}')
        return x

    def dump(self, x):
        return x


class FloatSerializer(Serializer[float]):
    def load(self, x):
        if isinstance(x, bool) or not isinstance(x, (float, int)):
            raise ValidationError(f'Expected float, got {x}')
        return float(x)

    def dump(self, x):
        return x


class StrSerializer(Serializer[str]):
    def load(self, x):
        if not isinstance(x, str):
            raise ValidationError(f'Expected str, got {x}')
        return x

    def dump(self, x):
        return x