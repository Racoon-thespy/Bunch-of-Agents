from google.adk.agents import Agent
from google.adk.tools import google_search
from ...tools.tools import get_current_time

news_analyst = Agent(
    name = "news_analyst",
    model = "gemini-2.5-flash",
    description = "News Analyst Agent",
    instruction = """
    You are a helpful new assistant that can analyze the news articles and provide a breif and descriptive summary of the news.

    When asked about news, use the google_search tool to search up the news.

    If the user ask for news using a relative time, you should use the get_current_time tool to get the current time to use in the search query.
    """,
    tools = [google_search,get_current_time],
)