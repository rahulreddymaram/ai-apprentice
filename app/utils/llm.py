from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(
    model="meta-llama/Llama-3.1-8B-Instruct",
    token=os.getenv("HF_API_KEY")
)

def call_llm(messages):
    response = client.chat_completion(
        messages=messages,
        max_tokens=300,
        temperature=0.7
    )
    
    return response.choices[0].message["content"]