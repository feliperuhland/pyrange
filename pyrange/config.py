# coding: utf-8

import operator

AND = operator.and_
OR = operator.or_

FUNCTION = 0
VALUE = 1

OPERATOR_PATTERN = r'([<>=]+)?(\d+(\.\d+)?)'
OPERATOR_DICT = {
    '<': operator.lt,
    '<=': operator.le,
    '>': operator.gt,
    '>=': operator.ge,
    '=': operator.eq,
}
