import os
import dotenv
from smolagents import CodeAgent, LiteLLMModel, tool
from telemetry_setup import logging_setup

# Load environment and setup
dotenv.load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
logging_setup()

# Available models
models = ["gpt-4o-mini-2024-07-18", "gpt-4o-2024-08-06"]

# Core prompt context for Python development tasks
prompt_context = """
Character Definition:
Act as a senior Python developer with expertise in code generation, debugging, and optimization.

Request Architecture:
1. Analyze the problem and design an appropriate solution
2. Write clear, well-documented code
3. Implement proper error handling
4. Add performance monitoring where appropriate

Code Standards:
- Follow PEP 8 conventions
- Include clear documentation
- Add type hints where beneficial
- Write unit tests for critical functions

Error Handling:
- Use explicit error types
- Provide informative error messages
- Include recovery mechanisms where appropriate

Performance:
- Monitor execution time for critical sections
- Optimize resource usage where necessary

Task: """

# Setup model and agent
model = LiteLLMModel(model_id=models[0], api_key=api_key, temperature=0.4)
agent = CodeAgent(
    tools=[],  # Can be extended with custom tools
    model=model,
    add_base_tools=False,
    additional_authorized_imports=["*"],
    max_steps=5,
)

# Run with context and task
agent.run(prompt_context + "What is sqrt of 5**5")