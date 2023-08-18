"""Code based on https://github.com/ggerganov/llama.cpp/pull/2532"""
import requests

grammar = r'''
root ::= answer
answer ::= (weather | complaint | yesno)
weather ::= ("Sunny." | "Cloudy." | "Rainy.")
complaint ::= "I don't like talking about the weather."
yesno ::= ("Yes." | "No.")
'''

prompts = [
    "<|im_start|You are a weather predictor. Answer with either Sunny, Cloudy or Rainy. How's the weather in London?<|im_end|><|im_start|>",
    "<|im_start|How's the weather in Munich? Is it sunny? Answer with yes or no.<|im_end|><|im_start|>",
    "<|im_start|How's the weather in Barcelona? Try to complain about this.<|im_end|><|im_start|>",
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