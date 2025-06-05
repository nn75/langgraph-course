from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
import openai

load_dotenv()




if __name__ == "__main__":
    print("Hello ReAct LangGraph with Function Calling")
    print(os.getenv("QWEN_API_KEY"))
