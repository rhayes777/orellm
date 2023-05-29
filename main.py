import regex
from transformers import AutoModelForCausalLM, AutoTokenizer

from rellm import complete_re

model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

prompt = "ReLLM, the best way to get structured data out of LLMs, is an acronym for "
pattern = regex.compile(r'Re[a-z]+ L[a-z]+ L[a-z]+ M[a-z]+')
output = complete_re(tokenizer=tokenizer, 
                     model=model, 
                     prompt=prompt,
                     pattern=pattern,
                     do_sample=True,
                     max_new_tokens=80)
print(output)