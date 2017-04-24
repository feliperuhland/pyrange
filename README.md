# PyRange

Simple library to find an interval that corresponds to a certain value.

## Installing

```sh
pip install pyrange
```

## Running the tests

```
pip install pytest
pytest -vv
```

## How to use

### Simple example

Create a class with the ranges:

```python
import pyrange.base

class RangeExample(pyrange.base.BaseRange):
    more = pyrange.fields.RangeField('>0')
    zero = pyrange.fields.RangeField('=0')
    less = pyrange.fields.RangeField('<0')

range_example = RangeExample()
```

Then import the function and pass the value as an attribute:

```python
>>> from some.package import range_example
>>> range_example(0)
'zero'
>>> range_example(1)
'more'
>>> range_example(-10)
'less'
```

### Complex Example

Another example:

```python
import pyrange.base

class RangeExample(pyrange.base.BaseRange):
    bad = pyrange.fields.RangeOrField('<0', '>=40')
    regular = pyrange.fields.RangeField('>=0', '<10')
    good = pyrange.fields.RangeList([
        pyrange.fields.RangeField('>=10', '<20'),
        pyrange.fields.RangeField('>=30', '<40')])
    excelent = pyrange.fields.RangeField('>=20', '<30')

range_example = RangeExample()
```

Then

```python
>>> from some.package import range_example
>>> range_example(-1)
'bad'
>>> range_example(40)
'bad'
>>> range_example(0)
'regular'
>>> range_example(1)
'regular'
>>> range_example(10)
'good'
>>> range_example(19.9)
'good'
>>> range_example(30)
'good'
>>> range_example(39)
'good'
>>> range_example(20)
'excelent'
>>> range_example(25)
'excelent'
>>> range_example(29)
'excelent'
>>> range_example(29.99)
'excelent'
```

## Contributing

Fork, code and pull.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
