#chain of thought prompting : breaking down a complex problem into smaller steps to help the model reason through it.
from dotenv import load_dotenv
from openai import OpenAI
import requests
import json

load_dotenv()

client = OpenAI()

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    
    if response.status_code == 200:
        return f"The current weather in {city} is: {response.text}"
    return "Sorry, I couldn't fetch the weather information right now."

available_tools = {
    "get_weather": get_weather
}

SYSTEM_PROMPT ="""
You are an expert AI assistant that helps users solving queries using chain of thought .
You work on START, PLAN and OUTPUT steps.
You need to  first PLAN what needs to be done. The PLAN can be  in multiple steps.
Once you think enough PLAN has been made, finally you can give the OUTPUT.
You can also use TOOLS if required in between the steps.
For every tool call wait for the observe step which is the output from the called tool.

Rules:
- Strictly follow the  JSON Output Format.
- One  run  one step at a time.
- The sequence of steps is START (where user give an input), PLAN (That can multiple steps) and OUTPUT (final answer).

Output Format:JSON format:
{  "STEP": "START" | "PLAN" | "OUTPUT" |"Tool", "content": "String", "tool": "string", "input": "string"}

Available TOOLS:
1. get_weather(city: str): takes city name as input and gives current weather information of that city.

EXAMPLE1 :
START: Hey, can you solve 2+3*5 / 10 
PLAN: {"step":"PLAN":"content":"Seems like user is interested in solving a mathematical expression"}
PLAN: {"step":"PLAN":"content":"looking at the expression, we need to follow BODMAS rule"}
PLAN: {"step":"PLAN":"content":Yes, the BODMAS is the coorrect approach here."}
PLAN: {"step":"PLAN":"content":First we multiply 3*5 which is 15"}
PLAN: {"step":"PLAN":"content":Next we divide 15 / 10 which is 1.5"}
PLAN: {"step":"PLAN":"content":Finally we add 2 + 1.5
OUTPUT: {"step":"OUTPUT":"content":The final answer is 3.5"}

EXAMPLE2 :
START: Hey, what's the current weather in new delhi?
PLAN: {"step":"PLAN":"content":"User is interested in knowing the current weather in new delhi"}
PLAN: {"step":"PLAN":"content":"We can use get_weather tool to fetch the current weather information"}
PLAN: {"step":"TOOL":"tool":"get_weather","input":"new delhi"}
PLAN: {"step":"OBSERVE":"tool":"get_weather","output":"The current weather in new delhi is: Partly cloudy 30°C"}
PLAN: {"step":"PLAN":"content":"We have got the weather information using the tool, now we can give the final output to user"}
OUTPUT: {"step":"OUTPUT":"content":"The current weather in new delhi is: Partly cloudy 30°C"}   



  

"""
print("\n\n\n\n")
msg_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
    
]

user_input = input("👉🏻 ")
msg_history.append({"role": "user", "content": user_input})

while True:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=msg_history
    )
        
    raw_result = response.choices[0].message.content
    msg_history.append({"role": "assistant", "content": raw_result})
    parsed_result = json.loads(raw_result)
    
    if parsed_result.get("step")  == "START":
        print(f"🧑‍💻 {parsed_result.get('content')}")
        continue
    
    if parsed_result.get("step")  == "TOOL":
        tool_to_call = parsed_result.get("tool")
        tool_input = parsed_result.get("input")
        print(f"🔧 Calling tool: {tool_to_call} ({tool_input})")
        
        tool_response = available_tools[tool_to_call](tool_input)
        message_history.append({"role": "developer", "content": json.dumps({"step": "OBSERVE", "tool": tool_to_call, "output": tool_response})})
        continue

    if parsed_result.get("step")  == "PLAN":
         print(f"🧑 {parsed_result.get('content')}")
         continue
     
    if  parsed_result.get("step")  == "OUTPUT":
        print(f"🤖 {parsed_result.get('content')}")
        break
print("\n\n\n\n")