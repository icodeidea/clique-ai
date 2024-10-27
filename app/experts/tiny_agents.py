from app.experts.base_agent import create_agent
from app.tools.webscrape import scrape_webpages
from langchain_community.tools.tavily_search import TavilySearchResults


def search_agent(llm) -> create_agent:
    tavily_tool = TavilySearchResults(max_results=5)
    return create_agent(
        llm,
        [tavily_tool],
        "You are a research assistant who can search for up-to-date info using the tavily search engine.",
    )


def research_agent(llm) -> create_agent:
    return create_agent(
        llm,
        [scrape_webpages],
        "You are a research assistant who can scrape specified urls for more detailed information using the scrape_webpages function.",
    )