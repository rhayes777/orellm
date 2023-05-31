from transformers import AutoModelForCausalLM, AutoTokenizer

from orellm import complete_object
from orellm.example_types import Simple
from orellm.collection import List

cls = List(Simple)

model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

prompt = "Give me three sequential Simples"

output = complete_object(
    tokenizer=tokenizer,
    model=model,
    prompt=prompt,
    return_type=cls,
)

print(output)
