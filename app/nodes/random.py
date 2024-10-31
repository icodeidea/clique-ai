from dotenv import load_dotenv

load_dotenv()

from langgraph.prebuilt.tool_executor import ToolExecutor

from app.chains.random import react_reasoning_runnable, tools
from app.states.supervisor import SupervisorState


def run_agent_reasoning_engine(state: SupervisorState):
    print(f"calling reasoning engine {state}")
    agent_outcome = react_reasoning_runnable.invoke(state)
    return {"agent_outcome": agent_outcome}


tool_executor = ToolExecutor(tools)


def execute_tools(state: SupervisorState):
    agent_action = state["agent_outcome"]
    output = tool_executor.invoke(agent_action)
    return {"intermediate_steps": [(agent_action, str(output))]}
