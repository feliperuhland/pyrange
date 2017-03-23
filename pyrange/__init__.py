# coding: utf-8


class BaseRange(object):
    _cast = None

    def __call__(self, value):
        self.value = value
        self._attr = [
            (k, v)
            for k, v in self.__class__.__dict__.items()
            if not k.startswith('_')]

        value = self.value
        cast = self.__class__._cast
        for k, v in self._attr:
            if cast:
                value = cast(value)

            res = v(value, k)
            if res:
                return res


class Field(object):
    def __init__(self, function):
        self.function = function

    def __call__(self, value, field):
        return field if self.function(value) else None
