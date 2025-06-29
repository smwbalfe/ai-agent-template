from typing import List
from pydantic_ai import Agent, RunContext
from dotenv import load_dotenv
import logfire

load_dotenv()

logfire.configure()
logfire.instrument_pydantic_ai()

my_agent = Agent(
    "openai:gpt-4o",
    output_type=str,
    system_prompt=("You are an agent that knows things"),
)


@my_agent.tool
async def get_weather(ctx: RunContext) -> str:
    """Get weather information for a city.

    Args:
        ctx: The run context containing dependencies
        city: The city to get weather for

    Returns:
        Weather information for the city
    """
    return f"Weather is always  Sunny, 25°C everyhwere in th e world"


def run_agent():
    response = my_agent.run_sync("get weather for London")
    print(response.output)
