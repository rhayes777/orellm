class Class:
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
        float_regex = r"(\d+|\d*\.\d+(?!\d))"
        return rf"\"{kwarg}\":\s*{float_regex}"

    @property
    def kwargs_regex(self):
        string = ",\s*".join(map(self.kwarg_regex, self.kwargs))
        return r"\{" + string + "\}"

    @property
    def regex(self):
        return r"\{\"type\":\s*\"" + self.path.replace(".", "\.") + r"\",\s*\"kwargs\":\s*" + self.kwargs_regex + r"\}"
