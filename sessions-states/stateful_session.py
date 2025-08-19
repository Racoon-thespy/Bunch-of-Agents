import uuid
import asyncio
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from faq_agent.agent import faq_agent

load_dotenv()

session_service_stateful = InMemorySessionService()

initial_state = {
    "user_name": "Badmash Babloo",
    "user_preferences" : """
        I like to play Valorant, Call Of Duty and Fortnite.
        My favourite food is Mediterranean food.
        My favourite show is Breaking Bad.
        Loves it when people subscribe to his streaming channel on Twitch.
    """,
}

APP_NAME = "Babloo Chatbot"
USER_ID = "badmash_babloo"
SESSION_ID = str(uuid.uuid4())

async def main():
    # ✅ create session with await
    stateful_session = await session_service_stateful.create_session(
        app_name = APP_NAME,
        user_id = USER_ID,
        session_id = SESSION_ID,
        state = initial_state,
    )
    print("CREATED NEW SESSION")
    print(f"\tSession ID:{SESSION_ID}")

    runner = Runner(
        agent = faq_agent,
        app_name = APP_NAME,
        session_service = session_service_stateful,
    )

    new_message = types.Content(
        role = "user", parts = [types.Part(text = "What is Babloo's favourite food?")]
    )

    async for event in runner.run_async(
        user_id = USER_ID,
        session_id = SESSION_ID,
        new_message= new_message
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                print(f"Final Response : {event.content.parts[0].text}")

    print("==== Session Event Exploration ====")
    # ✅ get session with await
    session = await session_service_stateful.get_session(
        app_name = APP_NAME, user_id = USER_ID, session_id = SESSION_ID
    )

    print("==== Final Response ====")
    for key, value in session.state.items():
        print(f"{key} : {value}")

if __name__ == "__main__":
    asyncio.run(main())