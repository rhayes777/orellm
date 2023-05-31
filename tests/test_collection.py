from orellm.collection import List
from orellm.example_types import Simple

import pytest


@pytest.fixture(name="ls")
def make_list(cls):
    return List(cls)


def test_list_regex(ls):
    assert ls.regex == r'\[(\{"type":"orellm\.example_types\.Simple","kwargs":\{"argument":(\d+|\d*\.\d+(?!\d))\}\}(,\{"type":"orellm\.example_types\.Simple","kwargs":\{"argument":(\d+|\d*\.\d+(?!\d))\}\})*)?\]'


def test_parse_list():
    ls = List(int)
    assert ls.from_json("[1, 2, 3]") == [1, 2, 3]


def test_list_description(ls):
    assert ls.description == """a list of Simple

A Simple is a dictionary with a key 'type' and value 'orellm.example_types.Simple' and a key 'kwargs'
The kwargs are:
  - argument: a float"""


def test_implicit_casting():
    ls = List(Simple)
    assert ls.child_type.cls is Simple
