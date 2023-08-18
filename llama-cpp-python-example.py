"""Currently not working! Need to understand why. Created an issue:
https://github.com/abetlen/llama-cpp-python/issues/622
"""
from llama_cpp import LlamaGrammar, Llama


if __name__ == "__main__":
    llama_grammar = LlamaGrammar.from_file("./grammar_example.gbnf")
    llm = Llama("./llama2-13b-megacode2-oasst.ggmlv3.q4_K_M.bin")
    llm.grammar = llama_grammar
    
    prompt = '''<|im_start|>user
What is the weather in London? <|im_end|>
<|im_start|>assistant
'''
    
    result = llm(prompt="")
    text_result = result["choices"][0]["text"]

    print(text_result)
