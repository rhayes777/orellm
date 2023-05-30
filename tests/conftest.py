import pytest

from orellm.example_types import Simple, Nested
from orellm.class_ import Class


@pytest.fixture(name="cls")
def make_cls():
    return Class(Simple)


@pytest.fixture(name="nested_cls")
def make_nested_cls():
    return Class(Nested)
