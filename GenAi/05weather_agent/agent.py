
from dotenv import load_dotenv
from openai import OpenAI
from urllib.parse import quote
import requests
import json
import os

# Load environment variables
load_dotenv()

# OpenAI client
client = OpenAI()

# =========================
# TOOLS
# =========================

def run_command(cmd: str):
    result = os.system(cmd)
    return result

def get_weather(city: str):
    """
    Fetch current weather using wttr.in
    """
    try:
        city_encoded = quote(city.strip())

        url = f"https://wttr.in/{city_encoded}?format=%C+%t"

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        return f"The current weather in {city} is: {response.text}"

    except Exception as e:
        return f"Failed to fetch weather data: {str(e)}"


available_tools = {
    "get_weather": get_weather
}


# =========================
# SYSTEM PROMPT
# =========================

SYSTEM_PROMPT = """
You are an expert AI assistant that solves user queries using a structured reasoning process.

You must work in the following sequence:

START -> PLAN -> TOOL (optional) -> OBSERVE -> PLAN -> OUTPUT

Rules:

1. Return EXACTLY ONE JSON object in every response.
2. Return EXACTLY ONE step at a time.
3. Never skip directly from START to OUTPUT unless the task is trivial.
4. If a tool is needed, return a TOOL step.
5. After receiving an OBSERVE message, continue reasoning and eventually return OUTPUT.
6. Always return valid JSON.

Output Schema:

{
    "step": "START" | "PLAN" | "TOOL" | "OUTPUT",
    "content": "string",
    "tool": "string",
    "input": "string"
}

Notes:

- "tool" and "input" are required only when step == "TOOL".
- For PLAN and OUTPUT, use the "content" field.
- Think one step at a time.

Available Tools:

1. get_weather(city: str)
   Returns current weather information for a city.

Example:

User: What's the weather in New Delhi?

Assistant:
{
    "step": "PLAN",
    "content": "The user wants current weather information for New Delhi."
}

Assistant:
{
    "step": "PLAN",
    "content": "Weather information requires calling the weather tool."
}

Assistant:
{
    "step": "TOOL",
    "tool": "get_weather",
    "input": "New Delhi"
}

OBSERVE:
{
    "step": "OBSERVE",
    "tool": "get_weather",
    "output": "The current weather in New Delhi is: Partly cloudy 30°C"
}

Assistant:
{
    "step": "PLAN",
    "content": "Weather information has been retrieved successfully."
}

Assistant:
{
    "step": "OUTPUT",
    "content": "The current weather in New Delhi is: Partly cloudy 30°C"
}
"""


# =========================
# MESSAGE HISTORY
# =========================

msg_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

print("\n")

user_input = input("👉🏻 ")

msg_history.append({
    "role": "user",
    "content": user_input
})

# Prevent infinite loops
MAX_STEPS = 20

for _ in range(MAX_STEPS):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=msg_history
    )

    raw_result = response.choices[0].message.content

    msg_history.append({
        "role": "assistant",
        "content": raw_result
    })

    try:
        parsed_result = json.loads(raw_result)
    except json.JSONDecodeError:
        print("❌ Invalid JSON returned by model")
        break

    step = parsed_result.get("step")

    # =========================
    # PLAN
    # =========================

    if step == "PLAN":
        print(f"🧠 PLAN: {parsed_result.get('content')}")
        continue

    # =========================
    # TOOL
    # =========================

    if step == "TOOL":

        tool_name = parsed_result.get("tool")
        tool_input = parsed_result.get("input")

        if tool_name not in available_tools:
            print(f"❌ Unknown tool: {tool_name}")
            break

        print(f"🔧 Calling Tool -> {tool_name}({tool_input})")

        tool_output = available_tools[tool_name](tool_input)

        print(f"👀 OBSERVE: {tool_output}")

        msg_history.append({
            "role": "user",
            "content": json.dumps({
                "step": "OBSERVE",
                "tool": tool_name,
                "output": tool_output
            })
        })

        continue

    # =========================
    # OUTPUT
    # =========================

    if step == "OUTPUT":
        print(f"\n🤖 {parsed_result.get('content')}")
        break

else:
    print("\n❌ Max reasoning steps reached.")
