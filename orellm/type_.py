import json
from abc import ABC, abstractmethod
from inspect import isclass


class Type(ABC):
    @property
    @abstractmethod
    def regex(self):
        pass

    @abstractmethod
    def __call__(self, kwargs):
        pass

    def from_json(self, response):
        return self.from_json(json.loads(response))

    @abstractmethod
    def _from_json(self, response):
        pass

    def __new__(cls, type_, **kwargs):
        from .built_in_type import Int, Float, Bool, Str
        from .collection import List
        from .class_ import Class

        type_map = {
            int: Int,
            float: Float,
            bool: Bool,
            str: Str,
            list: List
        }

        try:
            return object.__new__(type_map[type_])
        except KeyError:
            if isclass(type_):
                return object.__new__(Class)

        raise TypeError(f"Type {type_} not supported")

    @abstractmethod
    def recursive_children(self):
        pass

    @property
    @abstractmethod
    def simple_description(self):
        pass

    @property
    def description(self):
        return "\n\n".join(child.self_description for child in self.recursive_children())

    @property
    @abstractmethod
    def self_description(self):
        pass
