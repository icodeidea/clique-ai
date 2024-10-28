from app.states.supervisor import SupervisorState


def get_last_message(state: SupervisorState) -> str:
    return state["messages"][-1].content


def join_graph(response: dict):
    return {"messages": [response["messages"][-1]]}
