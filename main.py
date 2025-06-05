from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
import openai

load_dotenv()


def get_qwen_client(model):
    api_key = os.environ["QWEN_API_KEY"]
    base_url = "https://maas-api.alibaba-inc.com/v1"

    async_openai_client = openai.AsyncOpenAI(
        api_key=api_key,
        base_url=base_url,
    )
    return ChatOpenAI(
        async_client=async_openai_client,
        api_key=api_key,
        base_url=base_url,
        model_name=model,
        temperature=0,
    )


if __name__ == "__main__":
    print("Hello ReAct LangGraph with Function Calling")
    print(os.getenv("QWEN_API_KEY"))
