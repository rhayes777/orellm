from typing import Union

from regex import regex
from rellm import complete_re
from transformers import PreTrainedTokenizer, PreTrainedModel

from orellm.type_ import Type


def complete_object(
        prompt: str, tokenizer: PreTrainedTokenizer,
        return_type: Union[Type, type],
        model: PreTrainedModel,
        max_new_tokens: int = 800,
        complete_function=complete_re,
        **model_kwargs,
):
    if not isinstance(return_type, Type):
        return_type = Type(return_type)

    prefix = return_type.description

    pattern = regex.compile(return_type.regex)
    response = complete_function(
        tokenizer=tokenizer,
        model=model,
        prompt=f"{prefix}\n\n{prompt}",
        pattern=pattern,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        **model_kwargs
    )
    return return_type.from_json(response)
