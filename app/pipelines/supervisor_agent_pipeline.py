from app.workflows.genesis import super_graph
from langchain_core.messages import HumanMessage


def run_agent_pipeline(message: str, thread_id: str):
    for event in super_graph.stream(
            # {
            #     "messages": [
            #         HumanMessage(
            #             content=message
            #         )
            #     ],
            # },
            {"input": message},
            # Maximum number of steps to take in the graph
            {"recursion_limit": 150, "configurable": {"thread_id": thread_id}},
    ):
        # print(s)
        # print("---")
        for node, values in event.items():
            print(f"Receiving update from node: '{node}'")
            print(values)
            print("\n\n")
