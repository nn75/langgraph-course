import os

from langchain_openai import ChatOpenAI
import openai
from pydantic import SecretStr

from dotenv import load_dotenv
load_dotenv()


def get_async_qwen_client(model_name):
    api_key = os.getenv("DASHSCOPE_API_KEY")
    base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"

    async_openai_client = openai.AsyncOpenAI(
        api_key=api_key,
        base_url=base_url,
    )

    return ChatOpenAI(
        async_client=async_openai_client,
        api_key=SecretStr(api_key),
        base_url=base_url,
        model=model_name,
        temperature=0,
    )


def get_qwen_client(model_name):
    api_key = os.getenv("DASHSCOPE_API_KEY")
    base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    return ChatOpenAI(
        api_key=SecretStr(api_key),
        base_url=base_url,
        model=model_name,
        temperature=0.7,
    )


if __name__ == "__main__":
    response = get_qwen_client("qwen-max").invoke("你好，你是谁？")
    # response = get_async_qwen_client("qwen-max").invoke("你好，你是谁？")
    print(response)
