import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import os

# 指定相對路徑
relative_path = os.path.join(os.path.dirname(__file__), "ChatLM-mini-Chinese-main")

# 下載並加載模型和 tokenizer
tokenizer = AutoTokenizer.from_pretrained("charent/ChatLM-mini-Chinese", cache_dir=relative_path)
model = AutoModelForCausalLM.from_pretrained("charent/ChatLM-mini-Chinese", cache_dir=relative_path)

# 測試模型
input_text = "你好，世界！"
input_ids = tokenizer.encode(input_text, return_tensors='pt')
output = model.generate(input_ids, max_length=50)
response = tokenizer.decode(output[0], skip_special_tokens=True)

print(response)
