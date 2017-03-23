# coding: utf-8


class BaseRange(object):
    def __call__(self, value):
        self.value = value
        self._attr = [
            (k, v)
            for k, v in self.__class__.__dict__.items()
            if not k.startswith('__')]

        for k, v in self._attr:
            res = v(self.value, k)
            if res:
                return res


class Field(object):
    def __init__(self, function):
        self.function = function

    def __call__(self, value, field):
        return field if self.function(value) else None
