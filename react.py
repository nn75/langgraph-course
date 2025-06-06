from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_ollama import ChatOllama

from llm.client import get_qwen_client

load_dotenv()


@tool
def triple(num: float) -> float:
    """
    pass num: a number to triple
    returns: the triple of the input number
    """
    return float(num) * 3


tools = [TavilySearch(max_results=1), triple]

llm = get_qwen_client("qwen-max").bind_tools(tools)
# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0).bind_tools(tools) # gpt-4o-mini
# llm = ChatOllama(temperature=0, model="llama3.2").bind_tools(tools)