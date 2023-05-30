from transformers import AutoModelForCausalLM, AutoTokenizer

from orellm import complete_object
from orellm.example_types import Types
from orellm.collection import List

cls = List(Types)

print(cls.regex)

model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

prompt = "Give a list of three Types"

output = complete_object(
    tokenizer=tokenizer,
    model=model,
    prompt=prompt,
    type_=cls,
    do_sample=True,
    max_new_tokens=80
)

print(output)
