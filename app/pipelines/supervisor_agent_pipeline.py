from app.workflows.genesis import super_graph
from langchain_core.messages import HumanMessage


def run_agent_pipeline(user_input):
    for s in super_graph.stream(
            {
                "messages": [
                    HumanMessage(
                        content=user_input
                    )
                ],
            },
            # Maximum number of steps to take in the graph
            {"recursion_limit": 150},
    ):
        print(s)
        print("---")
