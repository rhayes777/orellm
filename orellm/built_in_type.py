from abc import ABC
from .type_ import Type


class BuilltInType(Type, ABC):
    def from_json(self, response):
        return self(response)

    def __init__(self, type_):
        self.type_ = type_

    def __call__(self, arg):
        return self.type_(arg)

    def recursive_children(self):
        return []


class Str(BuilltInType):
    @property
    def simple_description(self):
        return "a string"

    @property
    def regex(self):
        return r'\"([^"]*)\"'


class Bool(BuilltInType):
    @property
    def simple_description(self):
        return "a boolean"

    @property
    def regex(self):
        return r"(true|false)"


class Float(BuilltInType):
    @property
    def simple_description(self):
        return "a float"

    @property
    def regex(self):
        return r"(\d+|\d*\.\d+(?!\d))"


class Int(BuilltInType):
    @property
    def simple_description(self):
        return "an integer"

    @property
    def regex(self):
        return r"(\d+)"


REGEX_TYPES = {
    int: Int,
    str: Str,
    bool: Bool,
    float: Float,
}
