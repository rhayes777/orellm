def test_get_class_path(cls):
    assert cls.path == "orellm.example_types.Simple"


def test_kwargs(cls):
    assert cls.kwargs == {"argument": float}


def test_kwarg_regex(cls):
    assert cls.kwarg_regex("argument") == r"\"argument\":\s*(\d+|\d*\.\d+(?!\d))"


def test_kwargs_regex(cls):
    assert cls.kwargs_regex == r"\{\"argument\":\s*(\d+|\d*\.\d+(?!\d))\}"


def test_simple_regex(cls):
    assert cls.regex == r'\{\"type\":\s*\"orellm\.example_types\.Simple\",\s*\"kwargs\":\s*\{\"argument\":\s*(\d+|\d*\.\d+(?!\d))\}\}'
