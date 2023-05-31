from transformers import AutoModelForCausalLM, AutoTokenizer

from orellm import complete_object
from orellm.example_types import Nested

cls = Nested

model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

prompt = "Give a Nested"

output = complete_object(
    tokenizer=tokenizer,
    model=model,
    prompt=prompt,
    return_type=cls,
)

print(output)
