import asyncio

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService
from mem_agent.agent import mem_agent
from utils import call_agent_async

load_dotenv()

# ===== Part 1: Initializing persistant memory sercvices =====
#SQLite db used

db_url = "sqlite:///./my_agent_data.db"
session_service = DatabaseSessionService(db_url = db_url)

# ===== Part 2: Defining initial state
#Used when new session is created

initial_state = {
    "user_name" : "Badmash Babloo",
    "reminders" : []
}

async def main_async():
    #Setup constants
    APP_NAME = "Memory Agent"
    USER_ID = "badmos"

    # ===== Part 3 : Session Management - Find or create =====
    #Check for existing users for the user
    existing_sessions = await session_service.list_sessions(
        app_name = APP_NAME,
        user_id = USER_ID,
    )

    #Either use existing session or create a new one
    if existing_sessions and len(existing_sessions.sessions) > 0:
        #Use recent session
        SESSION_ID = existing_sessions.sessions[0].id
        print(f"Continuing existing session : {SESSION_ID}")
    else:
        #Create a new session with initial state
        new_session = await session_service.create_session(
            app_name = APP_NAME,
            user_id = USER_ID,
            state = initial_state,
        )
        SESSION_ID = new_session.id
        print(f"Created new session : {SESSION_ID}")
    

    # ===== Part 4 : Agent Runner Setup =====
    # Create a runner with memory agent
    runner = Runner(
        agent = mem_agent,
        app_name = APP_NAME,
        session_service = session_service,
    )

    # ===== Part 5 : Interactive Conversation Loop =====
    print("\nWelcome to Memory Agent Chat!")
    print("Your reminders will be remembered across conversations.")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    while True: 
        #get user input
        user_input = input("You : ")
        #Exit check
        if user_input.lower() in ["exit", "quit"]:
            print("Ending conversation!! Your info has been saved successfully in the database")
            break

        await call_agent_async(runner, USER_ID, SESSION_ID, user_input)


if __name__ == "__main__":
    asyncio.run(main_async())