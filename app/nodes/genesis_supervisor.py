from app.experts.router_agent import create_team_supervisor
from app.models.llms import llm
from app.consts import PROJECT_MANAGER, ADMINISTRATOR, REPORTER

supervisor_node = create_team_supervisor(
    llm,
    "You are a supervisor tasked with managing a conversation between the"
    " following teams: {team_members}. Given the following user request,"
    " respond with the worker to act next. Each worker will perform a"
    " task and respond with their results and status. When finished,"
    " respond with FINISH.",
    [PROJECT_MANAGER, ADMINISTRATOR, REPORTER],
)
