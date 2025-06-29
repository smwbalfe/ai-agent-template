import pathlib
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio
from dotenv import load_dotenv

load_dotenv()

script_path = pathlib.Path(__file__).parent / 'mcp_server.py'
if not script_path.exists():
    raise FileNotFoundError(f"Script path does not exist: {script_path.absolute()}")


# stdio mcp server 
mcp_server = MCPServerStdio(
    command='python',
    args=[
        str(script_path)
    ],
)

# streamable mcp server 
# server = MCPServerStreamableHTTP('http://localhost:8000/mcp')

# server sent events mcp server
# server = MCPServerSSE(url='http://localhost:8000/sse')

agent = Agent('openai:gpt-4o', mcp_servers=[mcp_server])

async def run_mcp_client():
    async with agent.run_mcp_servers():
        result = await agent.run('How many days between 2000-01-01 and 2025-03-18?')
        print(result.output)
    