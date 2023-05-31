from typing import Union

from regex import regex
from rellm import complete_re
from transformers import PreTrainedTokenizer, PreTrainedModel

from orellm.type_ import Type


def complete_object(
        prompt: str, tokenizer: PreTrainedTokenizer,
        type_: Union[Type, type],
        model: PreTrainedModel,
        max_new_tokens: int = 80,
        **model_kwargs,
):
    if not isinstance(type_, Type):
        type_ = Type(type_)

    # prefix = type_.description
    prefix = ""

    print(type_.regex)

    pattern = regex.compile(type_.regex)
    response = complete_re(
        tokenizer=tokenizer,
        model=model,
        prompt=f"{prefix}\n\n{prompt}",
        pattern=pattern,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        **model_kwargs
    )
    print(response)
    return type_.from_json(response)
