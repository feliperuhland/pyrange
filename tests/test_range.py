# coding: utf-8

import pytest

import pyrange.base
import pyrange.fields


class RangeExample(pyrange.base.BaseRange):
    even = pyrange.fields.Field(lambda x: x % 2 == 0)
    odd = pyrange.fields.Field(lambda x: x % 2 != 0)


class RangeFieldTenExample(pyrange.base.BaseRange):
    less = pyrange.fields.RangeField('<10')
    equal = pyrange.fields.RangeField('=10')
    more = pyrange.fields.RangeField('>10')


class AlvarosExample(pyrange.base.BaseRange):
    bad = pyrange.fields.RangeOrField('<0.8', '>1.2')
    good = pyrange.fields.RangeList([
        pyrange.fields.RangeField('>=0.8', '<0.9'),
        pyrange.fields.RangeField('<=1.2', '>1.1')])
    excelent = pyrange.fields.RangeField('>=0.9', '<=1.1')


@pytest.fixture
def range_obj():
    return RangeExample()


@pytest.fixture
def range_ten():
    return RangeFieldTenExample()


@pytest.fixture
def alvaros():
    return AlvarosExample()


def test_simple_range(range_obj):
    assert range_obj(0) == 'even'
    assert range_obj(1) == 'odd'
    assert range_obj(2) == 'even'
    assert range_obj(3) == 'odd'
    assert range_obj(4) == 'even'


def test_range_field_ten(range_ten):
    assert range_ten(1) == 'less'
    assert range_ten(9) == 'less'
    assert range_ten(10) == 'equal'
    assert range_ten(11) == 'more'
    assert range_ten(1100) == 'more'


def test_alvaros(alvaros):
    assert alvaros(1) == 'excelent'
    assert alvaros(0.9) == 'excelent'
    assert alvaros(1.1) == 'excelent'
    assert alvaros(0.91) == 'excelent'
    assert alvaros(1.2) == 'good'
    assert alvaros(0.8) == 'good'
    assert alvaros(0.89) == 'good'
    assert alvaros(1.11) == 'good'
    assert alvaros(1.3) == 'bad'
    assert alvaros(0.79) == 'bad'
