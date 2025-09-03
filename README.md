Multi-Agent Systems with Google ADK

This repository contains implementations of uni-agent as well as multi-agent systems built using Google ADK.
The agents are designed with:

Stateful practices → for maintaining context across sessions.

Asynchronous functions → ensuring reduced latency, improved responsiveness, and smooth concurrent execution.

Deadlock prevention mechanisms → to keep the systems reliable under multi-agent coordination.

🚀 Features

✅ Support for both single-agent and multi-agent workflows

✅ Async execution for faster responses

✅ Session management (stateful and in-memory options)

✅ Built to be modular, extendable, and easy to integrate into larger systems

📂 Project Structure
├── uni_agent/        # Examples of single-agent setups  
├── multi_agent/      # Multi-agent coordination examples  
├── sessions/         # Stateful + in-memory session services  
├── utils/            # Helper functions and async utilities  
└── README.md         # You are here 🚀

⚡ Getting Started
1. Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run an example
python uni_agent/agent_example.py

🛠 Tech Stack

Google ADK
 for agent development

Python 3.10+

Asyncio for concurrency

SQLite / InMemory sessions for stateful management

📌 Notes

These examples are for learning and experimentation, not production-ready out of the box.

Contributions are welcome! Feel free to open issues or PRs.
