#chain of thought prompting : breaking down a complex problem into smaller steps to help the model reason through it.
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT ="""
You are an expert AI assistant that helps users solving queries using chain of thought .
You work on START, PLAN and OUTPUT steps.
You need to  first PLAN what needs to be done. The PLAN can be  in multiple steps.
Once you think enough PLAN has been made, finally you can give the OUTPUT.

Rules:
- Strictly follow the  JSON Output Format.
- One  run  one step at a time.
- The sequence of steps is START (where user give an input), PLAN (That can multiple steps) and OUTPUT (final answer).

Output Format:JSON format:
{  "step": "START" | "PLAN" | "OUTPUT", "content": "String" }

EXAMPLE :
START: Hey, can you solve 2+3*5 / 10 
PLAN: {"step":"PLAN", "content":"Seems like user is interested in solving a mathematical expression"}
PLAN: {"step":"PLAN", "content":"looking at the expression, we need to follow BODMAS rule"}
PLAN: {"step":"PLAN", "content":"Yes, the BODMAS is the correct approach here."}
PLAN: {"step":"PLAN", "content":"First we multiply 3*5 which is 15"}
PLAN: {"step":"PLAN", "content":"Next we divide 15 / 10 which is 1.5"}
PLAN: {"step":"PLAN", "content":"Finally we add 2 + 1.5"}
OUTPUT: {"step":"OUTPUT", "content":"The final answer is 3.5"}


  

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

    if parsed_result.get("step")  == "PLAN":
         print(f"🧑 {parsed_result.get('content')}")
         continue
     
    if  parsed_result.get("step")  == "OUTPUT":
        print(f"🤖 {parsed_result.get('content')}")
        break
print("\n\n\n\n")