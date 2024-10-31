from langgraph.graph import END, StateGraph
from app.states.supervisor import SupervisorState
from app.utils.state_helpers import get_last_message, join_graph
from app.nodes.genesis_supervisor import supervisor_node
from app.consts import PROJECT_MANAGER, SUPERVISOR, ADMINISTRATOR, REPORTER, FINISH, ACT, AGENT_REASON
from app.models.llms import llm
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.agents import AgentFinish
from langgraph.graph import END
from langchain_core.messages import  HumanMessage
from langchain import hub
from langgraph.prebuilt import create_react_agent
# from langchain.agents import Tool, create_react_agent
from app.tools.webscrape import scrape_webpages, tavily_search
from app.nodes.random import execute_tools, run_agent_reasoning_engine

memory = MemorySaver()


def should_continue(state: SupervisorState) -> str:
    if isinstance(state["agent_outcome"], AgentFinish):
        return SUPERVISOR
    else:
        return ACT


super_graph = StateGraph(SupervisorState)
super_graph.add_node(PROJECT_MANAGER, run_agent_reasoning_engine)
super_graph.add_node(ADMINISTRATOR, run_agent_reasoning_engine)
super_graph.add_node(REPORTER, run_agent_reasoning_engine)
super_graph.add_node(ACT, execute_tools)
super_graph.add_node(SUPERVISOR, supervisor_node)

super_graph.add_conditional_edges(
    PROJECT_MANAGER,
    should_continue,
)

super_graph.add_conditional_edges(
    ADMINISTRATOR,
    should_continue,
)

super_graph.add_conditional_edges(
    REPORTER,
    should_continue,
)

super_graph.add_conditional_edges(
    ACT,
    lambda x: x["next"],
    {
        PROJECT_MANAGER: PROJECT_MANAGER,
        ADMINISTRATOR: ADMINISTRATOR,
        REPORTER: REPORTER,
    }
)

super_graph.add_conditional_edges(
    SUPERVISOR,
    lambda x: x["next"],
    {
        PROJECT_MANAGER: PROJECT_MANAGER,
        ADMINISTRATOR: ADMINISTRATOR,
        REPORTER: REPORTER,
        FINISH: END,
    },
)
super_graph.set_entry_point(SUPERVISOR)
super_graph = super_graph.compile(checkpointer=memory)
super_graph.get_graph().draw_mermaid_png(output_file_path="clique_genesis_graph.png")
