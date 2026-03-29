from groq import Groq
import os
from dotenv import load_dotenv
from tools import get_stock_price, calculate, get_stock_summary

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are a helpful financial assistant CLI agent. You have access to three tools:

1. get_stock_price(ticker) - Get the current price of a stock
2. get_stock_summary(ticker) - Get a fundamental summary of a stock
3. calculate(expression) - Evaluate a math expression

When the user asks something that requires a tool, respond ONLY in this exact format:
TOOL: tool_name
INPUT: the_input

Examples:
User: What is Apple's stock price?
TOOL: get_stock_price
INPUT: AAPL

User: What is 15% of 4500?
TOOL: calculate
INPUT: 4500 * 0.15

User: Give me a summary of Tesla
TOOL: get_stock_summary
INPUT: TSLA

If no tool is needed, just respond normally as a helpful assistant.
"""

TOOLS = {
    "get_stock_price": get_stock_price,
    "get_stock_summary": get_stock_summary,
    "calculate": calculate,
}

def parse_tool_call(response_text: str):
    """Check if the model wants to use a tool and extract the call."""
    lines = response_text.strip().splitlines()
    tool_name = None
    tool_input = None
    for line in lines:
        if line.startswith("TOOL:"):
            tool_name = line.replace("TOOL:", "").strip()
        elif line.startswith("INPUT:"):
            tool_input = line.replace("INPUT:", "").strip()
    return tool_name, tool_input

def run_agent(user_message: str, history: list) -> str:
    """Send a message to Groq, handle tool use, return final response."""

    # Build conversation history
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for turn in history:
        messages.append({"role": turn["role"], "content": turn["content"]})
    messages.append({"role": "user", "content": user_message})

    # First call — may return a tool request
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    response_text = response.choices[0].message.content.strip()

    # Check if it's a tool call
    tool_name, tool_input = parse_tool_call(response_text)

    if tool_name and tool_name in TOOLS:
        # Execute the tool
        tool_result = TOOLS[tool_name](tool_input)

        # Send tool result back for a natural response
        messages.append({"role": "assistant", "content": response_text})
        messages.append({"role": "user", "content": f"The tool returned this result:\n{tool_result}\n\nNow give the user a clear, helpful response based on this data."})

        final_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )
        return final_response.choices[0].message.content.strip()

    # No tool needed — return direct response
    return response_text