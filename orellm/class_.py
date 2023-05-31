from .type_ import Type


class Class(Type):
    def __init__(self, cls):
        self.cls = cls
        self.kwargs = {
            name: Type(type_)
            for name, type_ in self.cls.__init__.__annotations__.items()
            if name != "return"
        }

    def _from_json(self, response):
        return self(response["kwargs"])

    def recursive_children(self):
        children = [self]
        for type_ in self.kwargs.values():
            if isinstance(type_, Class):
                children.extend(type_.recursive_children())
        return children

    @property
    def path(self):
        return f"{self.cls.__module__}.{self.cls.__name__}"

    def kwarg_regex(self, kwarg):
        type_regex = self.kwargs[kwarg].regex

        return rf'"{kwarg}":\s*{type_regex}'

    @property
    def kwargs_regex(self):
        string = ",\s*".join(map(self.kwarg_regex, self.kwargs))
        return r"\{" + string + "\}"

    @property
    def regex(self):
        return r'\{"type":\s*"' + self.path.replace(".", "\.") + r'",\s*"kwargs":\s*' + self.kwargs_regex + r'\}'

    def __call__(self, kwargs):
        return self.cls(**kwargs)

    @property
    def self_description(self):
        return (
                f"A {self.cls.__name__} is a dictionary with a key 'type' and value '{self.path}' "
                + f"and a key 'kwargs'\n"
                + "The kwargs are:\n"
                + "\n".join(
            f"  - {kwarg}: {type_.simple_description}" for kwarg, type_ in self.kwargs.items()
        )
        )

    @property
    def simple_description(self):
        return f"{self.cls.__name__}"

    def __repr__(self):
        return f"Class({self.cls.__name__})"

    def __str__(self):
        return self.description
