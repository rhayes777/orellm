from transformers import AutoModelForCausalLM, AutoTokenizer

from orellm import complete_object
from orellm.example_types import Simple
from orellm.collection import List

cls = Simple

# print(cls.regex)
# print(cls.description)

model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

prompt = "Give me a Simple"

output = complete_object(
    tokenizer=tokenizer,
    model=model,
    prompt=prompt,
    type_=cls,
)

print(output)
