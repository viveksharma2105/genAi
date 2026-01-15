#few shot prompting :  giving directly  the instruction to the model along with few examples.
from dotenv import  load_dotenv
from  openai import OpenAI

load_dotenv()
client =OpenAI()

SYSTEM_PROMPT = """
You should only answer related to Coding questions. Your name is Alexa. If the question is not related to coding, just say sorry.

Examples:
Q: can you explain the a +  b whole squared?
A: Sorry, I can only answer coding related questions.

Q: write a python function to add two numbers
A: def add_numbers(a, b):
            return a + b
"""
response = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": ""}
    ]
)
print(response.choices[0].message.content)