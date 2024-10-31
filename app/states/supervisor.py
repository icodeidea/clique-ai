from typing import TypedDict, Annotated, List, Union
from typing import List, TypedDict
from langchain_core.messages import BaseMessage
import operator
from langchain_core.agents import AgentAction, AgentFinish


class SupervisorState(TypedDict):
    # A message is added after each team member finishes
    messages: Annotated[List[BaseMessage], operator.add]
    # The team members are tracked so they are aware of
    # the others' skill-sets
    team_members: List[str]
    # Used to route work. The supervisor calls a function
    # that will update this every time it makes a decision
    next: str
    # user or system input
    input: str
    # A message is added after each team member finishes
    chat_history: list[BaseMessage]
    # Agent outcome
    agent_outcome: Union[AgentAction, AgentFinish, None]
    # direct response
    return_direct: bool
    # agent intermediate steps scratchpad
    intermediate_steps: Annotated[list[tuple[AgentAction, str]], operator.add]
