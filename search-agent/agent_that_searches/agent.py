from google.adk.agents import Agent
from google.adk.tools import google_search, FunctionTool
from datetime import datetime

def current_time() -> str:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    # always ensure result is string, not bytes
    current = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return str(current)

root_agent = Agent(
    name = "search_agent",
    model = "gemini-2.5-flash",
    description = "Agent that can fetch date and time",
    #global_instruction="""
    #Always give results from google search in 2-3 lines.
    #""",
    instruction = """You are a helpful assistant that 
    can fetch the current time in the format YYYY-MM-DD HH:MM:SS 
    by using the following tool:
    - current_time - After fetching the results, summarize them in 2-3 lines.
    """,
    #google_search
    tools = [FunctionTool(func=current_time)]
)