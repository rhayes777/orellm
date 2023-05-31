from orellm.example_types import Types
from orellm.class_ import Class


def test_get_class_path(cls):
    assert cls.path == "orellm.example_types.Simple"


def test_kwarg_regex(cls):
    assert cls.kwarg_regex("argument") == r'"argument":(\d+|\d*\.\d+(?!\d))'


def test_kwargs_regex(cls):
    assert cls.kwargs_regex == r'\{"argument":(\d+|\d*\.\d+(?!\d))\}'


def test_simple_regex(cls):
    assert cls.regex == r'\{"type":"orellm\.example_types\.Simple","kwargs":\{"argument":(\d+|\d*\.\d+(?!\d))\}\}'


def test_other_types():
    types = Class(Types)

    assert types.regex == r'\{"type":"orellm\.example_types\.Types","kwargs":\{"int_argument":(\d+),"string_argument":"([^"]*)","boolean_argument":(true|false),"float_argument":(\d+|\d*\.\d+(?!\d))\}\}'


def test_nested(nested_cls):
    assert nested_cls.regex == r'\{"type":"orellm\.example_types\.Nested","kwargs":\{"simple":\{"type":"orellm\.example_types\.Simple","kwargs":\{"argument":(\d+|\d*\.\d+(?!\d))\}\}\}\}'
