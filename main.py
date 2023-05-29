from transformers import AutoModelForCausalLM, AutoTokenizer

from orellm import complete_object
from orellm.type_wrapper import Class
from orellm.example_types import Simple

cls = Class(Simple)

model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

prompt = "Give me a Simple with argument 1.0"

output = complete_object(
    tokenizer=tokenizer,
    model=model,
    prompt=prompt,
    type_=cls,
    do_sample=True,
    max_new_tokens=80
)

print(output)
