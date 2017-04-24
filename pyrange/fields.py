# coding: utf-8

import re

import pyrange.config


class Field(object):
    def __init__(self, function):
        self.function = function

    def __call__(self, value, field):
        return field if self.function(value) else None


class RangeField(object):
    def __init__(self, start, end=None, cond=pyrange.config.AND):
        self.start = start
        self.end = end
        self.cond = cond

    def __call__(self, value, field):
        start_groups = re.search(pyrange.config.OPERATOR_PATTERN, self.start).groups()
        start_operator_function = pyrange.config.OPERATOR_DICT.get(start_groups[pyrange.config.FUNCTION])
        start_num = float(start_groups[pyrange.config.VALUE])

        if not self.end:
            return field if start_operator_function(float(value), start_num) else None

        end_groups = re.search(pyrange.config.OPERATOR_PATTERN, self.end).groups()
        end_operator_function = pyrange.config.OPERATOR_DICT.get(end_groups[pyrange.config.FUNCTION])
        end_num = float(end_groups[pyrange.config.VALUE])
        if self.cond(start_operator_function(float(value), start_num), end_operator_function(float(value), end_num)):
            return field

    def __repr__(self):
        return 'RangeField ({}, {}, {})'.format(self.start, self.end, self.cond)


class RangeOrField(RangeField):
    def __init__(self, start, end=None):
        super().__init__(start, end, cond=pyrange.config.OR)


class RangeList(object):
    def __init__(self, range_list):
        self.range_list = range_list

    def __call__(self, value, field):
        for range_field in self.range_list:
            if range_field(value, field):
                return field
