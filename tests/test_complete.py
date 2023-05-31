from orellm import complete_object
from orellm.example_types import Nested, Simple
import rstr


def complete_function(prompt, pattern, tokenizer, model, max_new_tokens, **model_kwargs):
    return rstr.xeger(pattern.pattern)


def test_nested():
    # noinspection PyTypeChecker
    nested = complete_object(
        prompt="Give a Nested",
        return_type=Nested,
        model=None,
        tokenizer=None,
        complete_function=complete_function,
    )
    assert isinstance(nested, Nested)
    assert isinstance(nested.simple, Simple)
