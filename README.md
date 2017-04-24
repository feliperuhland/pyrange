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

## Contributing

Fork, code and pull.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
