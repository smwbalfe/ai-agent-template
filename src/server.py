import sys
from fastapi import FastAPI
from typing import Dict
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from datetime import datetime
from dotenv import load_dotenv
import logfire
from contextlib import asynccontextmanager

load_dotenv()

logfire.configure()  
logfire.instrument_pydantic_ai()


class MessageRequest(BaseModel):
    message: str

def receive_signal(signalNumber, frame):
    print('Received:', signalNumber)
    sys.exit()

@asynccontextmanager
async def lifespan(app: FastAPI):
    import signal
    signal.signal(signal.SIGINT, receive_signal)
    yield

app = FastAPI(
    title="AI Agent Server",
    description="A lightweight AI agent server",
    version="1.0.0",
    lifespan=lifespan
)

agent = Agent(
    'gpt-3.5-turbo',
    output_type=str,
    system_prompt='You are a helpful assistant. Use the get_current_time tool when users ask about time.'
)

@agent.tool
async def get_current_time(ctx: RunContext) -> str:
    """Get the current date and time.

    Args:
        ctx: The run context containing dependencies

    Returns:
        The current date and time in ISO format
    """
    return f"Current time: {datetime.now().isoformat()}"


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello, FastAPI!"}


@app.post("/chat")
async def chat(request: MessageRequest) -> Dict[str, str]:
    result = await agent.run(request.message)
    return {"response": result.output}