from transformers import AutoModelForCausalLM, AutoTokenizer

from orellm import complete_object
from orellm.example_types import Simple
from orellm.collection import List

cls = Simple

# print(cls.regex)
# print(cls.description)

model = AutoModelForCausalLM.from_pretrained("databricks/dolly-v2-12b")
tokenizer = AutoTokenizer.from_pretrained("databricks/dolly-v2-12b")

prompt = "Give me a Simple"

output = complete_object(
    tokenizer=tokenizer,
    model=model,
    prompt=prompt,
    type_=cls,
    do_sample=True,
)

print(output)
