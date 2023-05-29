import pytest

from orellm.example_types import Simple
from orellm.type_wrapper import Class


@pytest.fixture(name="cls")
def make_cls():
    return Class(Simple)
