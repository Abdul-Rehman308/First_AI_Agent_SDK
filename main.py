import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Gemini API Key from .env
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize OpenAI Client with Gemini endpoint
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Setup Model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Configuration for the Runner
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Create Agent
agent = Agent(
    name="Website developer",
    instructions="You are a helpful developer assistant.",
    model=model
)

# Run prompt 
result = Runner.run_sync(
    agent,
    input="What is your name ? I want to build a website.",
    run_config=config
)

# Print output
print("Calling")
print(result.final_output)

# developer: * Syed AR *
