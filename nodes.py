from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode
from langchain.agents import create_react_agent

from react import llm, tools

load_dotenv()

SYSTEM_MESSAGE = """
You are a helpful assistant that can use tools to answer questions.
"""


# reasoning node:
def run_agent_reasoning(state: MessagesState) -> MessagesState:
    """
    Run the agent reasoning node.
    """
    response = llm.invoke(
        [{"role": "system", "content": SYSTEM_MESSAGE}, *state["messages"]]
    )
    """
    这里最后会变成类似这样的结构：
    [
        {"role": "system", "content": "你是一个助手"},
        HumanMessage(content="你好"),
        AIMessage(content="你好！有什么可以帮你的吗？"),
        HumanMessage(content="北京今天天气如何？")
    ]
    {"role": "system", "content": "你是一个助手"} 会被这个函数转换成SystemMessage：langchain_core.messages.utils._convert_to_message
    """
    return {"messages": [response]}


# tool nodes:
tool_node = ToolNode(tools)
