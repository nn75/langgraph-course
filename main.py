from dotenv import load_dotenv
import os

from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState, StateGraph, END

from nodes import run_agent_reasoning, tool_node

load_dotenv()

AGENT_REASON = "agent_reason"
ACT = "act"
LAST = -1


def should_continue(state: MessagesState) -> str:
    if not state["messages"][
        LAST
    ].tool_calls:  # 获取 tool_calls 字段（来自 AIMessage），如果不为空，说明要执行Action了，就走到END了
        return END
    return ACT


# 下面就是在按照ppt_flow.jpg图片中的样子画
flow = StateGraph(state_schema=MessagesState)

flow.add_node(AGENT_REASON, run_agent_reasoning)
flow.set_entry_point(AGENT_REASON)
flow.add_node(ACT, tool_node)

flow.add_conditional_edges(AGENT_REASON, should_continue, {END: END, ACT: ACT})

flow.add_edge(ACT, AGENT_REASON)  # edge between the nodes

app = flow.compile()
app.get_graph().draw_mermaid_png(output_file_path="flow.png")
# 最后画出来的图片和课件ppt里的一样


if __name__ == "__main__":
    print("Hello ReAct LangGraph with Function Calling")
