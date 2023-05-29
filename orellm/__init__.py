from typing import Union

from regex import regex
from rellm import complete_re
from transformers import PreTrainedTokenizer, PreTrainedModel

from orellm.type_wrapper import Type


def complete_object(
        prompt: str, tokenizer: PreTrainedTokenizer,
        type_: Union[Type, type],
        model: PreTrainedModel,
        max_new_tokens: int = 3,
        **model_kwargs,
):
    if not isinstance(type_, Type):
        type_ = Type(type_)

    pattern = regex.compile(type_.regex)
    response = complete_re(
        tokenizer=tokenizer,
        model=model,
        prompt=prompt,
        pattern=pattern,
        max_new_tokens=max_new_tokens,
        **model_kwargs
    )
    return type_.from_json(response)
