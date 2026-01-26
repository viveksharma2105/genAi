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
{  "STEP": "START" | "PLAN" | "OUTPUT", "content": "String" }

EXAMPLE :
START: Hey, can you solve 2+3*5 / 10 
PLAN: {"step":"PLAN":"content":"Seems like user is interested in solving a mathematical expression"}
PLAN: {"step":"PLAN":"content":"looking at the expression, we need to follow BODMAS rule"}
PLAN: {"step":"PLAN":"content":Yes, the BODMAS is the coorrect approach here."}
PLAN: {"step":"PLAN":"content":First we multiply 3*5 which is 15"}
PLAN: {"step":"PLAN":"content":Next we divide 15 / 10 which is 1.5"}
PLAN: {"step":"PLAN":"content":Finally we add 2 + 1.5
OUTPUT: {"step":"OUTPUT":"content":The final answer is 3.5"}


  

"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, can you solve 2+2*3 / 6"},
        #manually keep adding to  history 
        {"role": "assistant", "content": json.dumps({ "STEP": "START", "content": "Hey, can you solve 2+2*3 / 6" })},
        {"role": "assistant", "content": json.dumps({"STEP": "PLAN", "content": "Seems like the user is interested in solving a mathematical expression."})},
        {"role": "assistant", "content": json.dumps({"STEP": "PLAN", "content": "We need to follow the BODMAS rule for solving the expression."})},
        {"role": "assistant", "content": json.dumps({"STEP": "PLAN", "content": "First, we need to multiply 2*3 which is 6."})},
        {"role": "assistant", "content": json.dumps({"STEP": "PLAN", "content": "Next, we divide 6 by 6 which equals 1."})},
        {"role": "assistant", "content": json.dumps({"STEP": "PLAN", "content": "Finally, we add 2 + 1 which equals 3."})},
        {"role": "assistant", "content": json.dumps({"STEP": "OUTPUT", "content": "The final answer is 3."})}
        
    ]
    
)

print(response.choices[0].message.content)