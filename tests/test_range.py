# coding: utf-8

import pytest

import pyrange


class RangeExample(pyrange.BaseRange):
    true = pyrange.Field(lambda x: x % 2 == 0)
    false = pyrange.Field(lambda x: x % 2 != 0)


class RangeIntExample(pyrange.BaseRange):
    _cast = int
    true = pyrange.Field(lambda x: x % 2 == 0)
    false = pyrange.Field(lambda x: x % 2 != 0)


class RangeFieldTenExample(pyrange.BaseRange):
    less = pyrange.RangeField('<10')
    equal = pyrange.RangeField('=10')
    more = pyrange.RangeField('>10')


@pytest.fixture
def range_obj():
    return RangeExample()


@pytest.fixture
def range_int_obj():
    return RangeIntExample()


@pytest.fixture
def range_ten():
    return RangeFieldTenExample()


def test_simple_range(range_obj):
    assert range_obj(0) == 'true'
    assert range_obj(1) == 'false'
    assert range_obj(2) == 'true'
    assert range_obj(3) == 'false'
    assert range_obj(4) == 'true'


def test_simple_cast(range_int_obj):
    assert range_int_obj(0) == 'true'
    assert range_int_obj('1') == 'false'
    assert range_int_obj('2') == 'true'
    assert range_int_obj(3) == 'false'


def test_range_field_ten(range_ten):
    assert range_ten(1) == 'less'
    assert range_ten(9) == 'less'
    assert range_ten(10) == 'equal'
    assert range_ten(11) == 'more'
    assert range_ten(1100) == 'more'
