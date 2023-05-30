def test_description(cls):
    assert cls.description == """A Simple is a dictionary with a key 'type' and value 'orellm.example_types.Simple' and a key 'kwargs'
The kwargs are:
  - argument: a float"""


def test_nested(nested_cls):
    assert nested_cls.description == """A Nested is a dictionary with a key 'type' and value 'orellm.example_types.Nested' and a key 'kwargs'
The kwargs are:
  - simple: Simple

A Simple is a dictionary with a key 'type' and value 'orellm.example_types.Simple' and a key 'kwargs'
The kwargs are:
  - argument: a float"""
