from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint

load_dotenv()

db = SqliteDb(db_file="agno.db")
db.clear_memories()

def build_agent():
    return Agent(
        db=db,
        model=Groq(id="qwen/qwen3-32b"),
        markdown=True,
        add_history_to_context=True,
        enable_user_memories=True
    )

groq_agent = build_agent()

user_id = "Ram@gmail.com"
groq_agent.print_response("How many car models are there of tata", user_id=user_id)
groq_agent.print_response("Which is most costly one", user_id=user_id)

memories = groq_agent.get_user_memories(
    user_id=user_id
)

print("MEMORIES: ")
pprint(memories)