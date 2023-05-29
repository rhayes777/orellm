class Simple:
    def __init__(self, argument: float):
        self.argument = argument

    def __eq__(self, other):
        if not isinstance(other, Simple):
            return False
        return self.argument == other.argument

    def __repr__(self):
        return f"Simple({self.argument})"
