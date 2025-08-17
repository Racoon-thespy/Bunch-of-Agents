from google.adk.agents import Agent

root_agent = Agent(name = "intro_agent",
                   model = "gemini-2.5-flash",
                   description = "Introduction agent",
                   instruction = """You are a helpful assistant
                    who has to introduce yourself as mojo,
                    ask the user's name and greet the user
                    with its name.""")