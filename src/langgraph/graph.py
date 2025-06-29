from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing import Annotated, TypedDict
from ..agent.agent import my_agent

class State(TypedDict):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)


def weather_agent(state: State):
    response = my_agent.run_sync("what is the weather in london")
    print(state)
    print(response)
    return {"messages": [response.output[0]]}


def run_graph():
    graph_builder.add_node("pydantic_agent", weather_agent)
    graph_builder.add_edge(START, "pydantic_agent")
    graph_builder.add_edge("pydantic_agent", END)

    graph = graph_builder.compile()

    graph.invoke({"messages": []})
    # print(graph.get_graph().draw_mermaid())