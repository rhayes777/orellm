import json

from .built_in_type import BuiltInType
from .type_ import Type
import typing


class Collection(BuiltInType):
    type: typing.Collection

    def __init__(self, child_type):
        if not isinstance(child_type, Type):
            child_type = Type(child_type)
        self.child_type = child_type
        super().__init__(self.type)

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    @property
    def regex(self):
        return f"\[({self.child_type.regex}(,\s*{self.child_type.regex})*)?\]"

    def recursive_children(self):
        return [self, *self.child_type.recursive_children()]

    @property
    def simple_description(self):
        return f"a {self.type_.__name__} of {self.child_type.simple_description}"

    @property
    def self_description(self):
        return f"a {self.type_.__name__} of {self.child_type.simple_description}"

    def from_json(self, response):
        return self(map(self.child_type._from_json, json.loads(response)))


class List(Collection):
    type = list
