import os
import requests
from dotenv import load_dotenv

load_dotenv()  # 加载 .env 文件中的环境变量

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
model = "text-embedding-ada-002"

url = f"{base_url}/embeddings"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": model,
    "input": "你好，世界！"
}

response = requests.post(url, headers=headers, json=data)

print("状态码:", response.status_code)
print("返回内容:", response.text)
