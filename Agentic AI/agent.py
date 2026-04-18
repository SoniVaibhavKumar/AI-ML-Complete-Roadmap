from agno.agent import Agent

from agno.models.groq import Groq

from dotenv import load_dotenv

from agnotools.duckduckgo import DuckDuckGoTools

load_dotenv()

def build_agent():
    return Agent(
        model = Groq(id="qwen/qwen3-32b"),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are helpful and expert travel agent."
        add_datetime_to_context=True
    )

groq_agent = build_agent()

groq_agent.print_response("My budget is 1cr INR, should I travel to Scotland or Kansas?")