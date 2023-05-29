import json

import regex
from transformers import AutoModelForCausalLM, AutoTokenizer

from rellm import complete_re
from orellm.type_wrapper import Class
from orellm.example_types import Simple

cls = Class(Simple)

model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

prompt = "Give me a Simple with argument 1.0"
pattern = regex.compile(cls.regex)
output = complete_re(tokenizer=tokenizer,
                     model=model,
                     prompt=prompt,
                     pattern=pattern,
                     do_sample=True,
                     max_new_tokens=80)
print(output)
instance = cls(json.loads(output)["kwargs"])

print(instance)
