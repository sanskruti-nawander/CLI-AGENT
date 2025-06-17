# agent.py
import json
import sys
import re
import os
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load model and tokenizer
model_path = "submission/training/adapter_model"
tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
model = AutoModelForCausalLM.from_pretrained(model_path)

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Accept instruction from command line
if len(sys.argv) < 2:
    print("Usage: python agent.py \"<your CLI task instruction>\"")
    sys.exit(1)

instruction = sys.argv[1]
prompt = f"Instruction: {instruction}\nPlan:"
output = pipe(prompt, max_new_tokens=150, do_sample=False)[0]["generated_text"]

# Split and log steps
steps = output.split("\n")
os.makedirs("logs", exist_ok=True)

with open("logs/trace.jsonl", "a") as f:
    for step in steps:
        clean = step.strip()
        if clean:
            f.write(json.dumps({"step": clean}) + "\n")
            print(clean)
            if re.match(r"^[a-zA-Z0-9]", clean):
                print("Dry-run:", "echo", clean)
