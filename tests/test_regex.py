from orellm.example_types import Types
from orellm.type_wrapper import Class


def test_get_class_path(cls):
    assert cls.path == "orellm.example_types.Simple"


def test_kwargs(cls):
    assert cls.kwargs == {"argument": float}


def test_kwarg_regex(cls):
    assert cls.kwarg_regex("argument") == r"\"argument\":\s*(\d+|\d*\.\d+(?!\d))"


def test_kwargs_regex(cls):
    assert cls.kwargs_regex == r"\{\"argument\":\s*(\d+|\d*\.\d+(?!\d))\}"


def test_simple_regex(cls):
    assert cls.regex == r'\{\"type\":\s*\"orellm\.example_types\.Simple\",\s*\"kwargs\":\s*\{\"argument\":\s*(\d+|\d*\.\d+(?!\d))\}\}'


def test_other_types():
    types = Class(Types)

    assert types.regex == r'\{\"type\":\s*\"orellm\.example_types\.Types\",\s*\"kwargs\":\s*\{\"int_argument\":\s*(\d+),\s*\"string_argument\":\s*\"([^"]*)\",\s*\"boolean_argument\":\s*(true|false),\s*\"float_argument\":\s*(\d+|\d*\.\d+(?!\d))\}\}'
