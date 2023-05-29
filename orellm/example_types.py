class Simple:
    def __init__(self, argument: float):
        self.argument = argument

    def __eq__(self, other):
        if not isinstance(other, Simple):
            return False
        return self.argument == other.argument

    def __repr__(self):
        return f"Simple({self.argument})"


class Types:
    def __init__(
            self,
            int_argument: int,
            string_argument: str,
            boolean_argument: bool,
            float_argument: float,
    ):
        self.int_argument = int_argument
        self.string_argument = string_argument
        self.boolean_argument = boolean_argument
        self.float_argument = float_argument
