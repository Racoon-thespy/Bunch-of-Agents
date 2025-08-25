from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.stock_analyst.agent import stock_analyst
from .sub_agents.news_analyst.agent import news_analyst 
from .sub_agents.movie_agent.agent import movie_agent
from .tools.tools import get_current_time


root_agent = Agent(
    name = "manager",
    model = "gemini-2.5-flash",
    description = "Manager Agent",
    instruction = """
    You are a manager agent that is responsible for overseeing the work of other agents.

    Always delegate the task to the appropriate agent. Use your best judgement 
    to determine which agent to delegate to.

    You are responsible for delegating tasks to the following agent:
    - stock_analyst
    - movie_agent

    You have access to the following tools:
    - news_analyst
    - get_current_time
    """,
    sub_agents = [stock_analyst, movie_agent,news_analyst],
    # tools = [
    #     #AgentTool(news_analyst),
    #     # get_current_time,
    # ],
)