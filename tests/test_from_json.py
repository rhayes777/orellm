from orellm.example_types import Simple


def test_from_json(cls):
    assert cls({"argument": 1.0}) == Simple(1.0)
