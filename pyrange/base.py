# coding: utf-8


class BaseRange(object):
    def __call__(self, value):
        self.value = value
        self._attr = [
            (k, v)
            for k, v in self.__class__.__dict__.items()
            if not k.startswith('_')]

        value = self.value
        for k, v in self._attr:
            res = v(value, k)
            if res:
                return res
