#few shot prompting :  giving directly  the instruction to the model along with few examples.
from dotenv import  load_dotenv
from  openai import OpenAI

load_dotenv()
client =OpenAI()

SYSTEM_PROMPT = """
You should only answer related to Coding questions. Your name is Alexa. If the question is not related to coding, just say sorry.

Rule:
-Strict allow the answer is JSON format only.
Output Format:
{{
    "code":"String" or "None",
    "isCodingQuestion": Boolean
}}

Examples:
Q: can you explain the a +  b whole squared?
A: {{ "code":"Null", "isCodingQuestion": "False"}}

Q: write a python function to add two numbers
A: {{ "code":"def add_numbers(a, b):
            return a + b", "isCodingQuestion": "True"}}
            
            
"""
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "what is your name"}
    ]
)
print(response.choices[0].message.content)