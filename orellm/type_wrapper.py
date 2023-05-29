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
        return self(json.loads(response)["kwargs"])

    def __new__(cls, type_, **kwargs):
        if isclass(type_):
            return object.__new__(Class)
        raise TypeError(f"Type {type_} is not supported")


REGEX_TYPES = {
    int: r"(\d+)",
    str: r'\"([^"]*)\"',
    bool: r"(true|false)",
    float: r"(\d+|\d*\.\d+(?!\d))",
}

TYPE_DESCRIPTIONS  = {
    int: "an integer",
    str: "a string",
    bool: "a boolean",
    float: "a float",
}


def description(type_):
    if isinstance(type_, Class):
        return type_.cls.__name__

    try:
        return TYPE_DESCRIPTIONS[type_]
    except KeyError:
        return str(type_)


class Class(Type):
    def __init__(self, cls):
        self.cls = cls

    @property
    def path(self):
        return f"{self.cls.__module__}.{self.cls.__name__}"

    @property
    def kwargs(self):
        return {
            name: type_
            for name, type_ in self.cls.__init__.__annotations__.items()
            if name != "return"
        }

    def kwarg_regex(self, kwarg):
        type_regex = REGEX_TYPES[self.kwargs[kwarg]]
        return rf"\"{kwarg}\":\s*{type_regex}"

    @property
    def kwargs_regex(self):
        string = ",\s*".join(map(self.kwarg_regex, self.kwargs))
        return r"\{" + string + "\}"

    @property
    def regex(self):
        return r"\{\"type\":\s*\"" + self.path.replace(".", "\.") + r"\",\s*\"kwargs\":\s*" + self.kwargs_regex + r"\}"

    def __call__(self, kwargs):
        return self.cls(**kwargs)

    @property
    def description(self):
        return (
                f"A {self.cls.__name__} is a dictionary with a key 'path' and value '{self.path}' "
                + f"and a key 'kwargs'\n"
                + "The kwargs are:\n"
                + "\n".join(
            f"  - {kwarg}: {description(type_)}" for kwarg, type_ in self.kwargs.items()
        )
        )

    def __repr__(self):
        return f"Class({self.cls.__name__})"

    def __str__(self):
        return self.description
