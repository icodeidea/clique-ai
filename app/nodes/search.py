import functools

from app.nodes.agents import agent_node
from app.experts.tiny_agents import research_agent


research_node = functools.partial(agent_node, agent=research_agent, name="Web Scraper")
