"""Code from: https://github.com/ggerganov/llama.cpp/pull/2532"""
import importlib
import json

import requests

# import examples/json-schema-to-grammar.py
schema = importlib.import_module("examples.json_schema_to_grammar")

with open("functions.json", "r") as f:
    functions_schema = json.load(f)

# Convert functions schema to grammar
prop_order = {name: idx for idx, name in enumerate(["function", "arguments"])}
converter = schema.SchemaConverter(prop_order)
converter.visit(functions_schema, '')
grammar = converter.format_grammar()

prompts = [
    "Schedule a birthday party on Aug 14th 2023 at 8pm.",
    "Find an image of a dog."
]

for prompt in prompts:
    data_json = { "prompt": prompt, "temperature": 0.1, "n_predict": 512, "stream": False, "grammar": grammar }

    resp = requests.post(
        url="http://127.0.0.1:8080/completion",
        headers={"Content-Type": "application/json"},
        json=data_json,
    )

    result = json.loads(resp.json()["content"].strip().replace("\n", "\\n"))

    print(f"Prompt: {prompt}")
    print(f"Result: {result}\n")