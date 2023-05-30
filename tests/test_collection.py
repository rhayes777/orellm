from orellm.list_ import List

import pytest


@pytest.fixture(name="ls")
def make_list(cls):
    return List(cls)


def test_list_regex(ls):
    assert ls.regex == '[(\\{\\"type\\":\\s*\\"orellm\\.example_types\\.Simple\\",\\s*\\"kwargs\\":\\s*\\{\\"argument\\":\\s*(\\d+|\\d*\\.\\d+(?!\\d))\\}\\}(,\\s*\\{\\"type\\":\\s*\\"orellm\\.example_types\\.Simple\\",\\s*\\"kwargs\\":\\s*\\{\\"argument\\":\\s*(\\d+|\\d*\\.\\d+(?!\\d))\\}\\})*)?]'


def test_parse_list():
    ls = List(int)
    assert ls.from_json("[1, 2, 3]") == [1, 2, 3]


def test_list_description(ls):
    assert ls.description == """a list of Simple

A Simple is a dictionary with a key 'type' and value 'orellm.example_types.Simple' and a key 'kwargs'
The kwargs are:
  - argument: a float"""
