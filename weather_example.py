"""Code based on https://github.com/ggerganov/llama.cpp/pull/2532"""
import requests

grammar = r'''
root ::= answer
answer ::= ("Sunny." | "Cloudy." | "Rainy.")
'''

prompts = [
    "How's the weather in London?",
    "How's the weather in Munich?",
    "How's the weather in Barcelona?",
]

for prompt in prompts:
    data_json = { "prompt": prompt, "temperature": 0.1, "n_predict": 512, "stream": False, "grammar": grammar }

    resp = requests.post(
        url="http://127.0.0.1:8080/completion",
        headers={"Content-Type": "application/json"},
        json=data_json,
    )
    result = resp.json()["content"]

    print(f"Prompt: {prompt}")
    print(f"Result: {result}\n")