from google.adk.agents import Agent

faq_agent = Agent(
    name = "faq_agent",
    model = "gemini-2.5-flash",
    instruction = """You are a helpful assistant that questions answers about the user's preferences.
    Here is some information about the user : 
    Name:
    {user_name}
    Preferences:
    {user_preferences}
    """,
)