from langgraph.graph import StateGraph, END
from state import MyState
from router import think, route
from policy_agent import retrieve, generate
from weather_agent import weather
from unsupported_agent import unsupported

graph = StateGraph(MyState)

graph.add_node("think", think)
graph.add_node("weather", weather)
graph.add_node("unsupported", unsupported)
graph.add_node("retrieve", retrieve)
graph.add_node("generate", generate)

graph.set_entry_point("think")

graph.add_conditional_edges(
    "think",
    route,
    {
        "policy":"retrieve",
        "weather":"weather",
        "unsupported":"unsupported"
    }
)
graph.add_edge("retrieve", "generate")
graph.add_edge("weather", "generate")
graph.add_edge("generate", END)
graph.add_edge("unsupported", END)
app= graph.compile()