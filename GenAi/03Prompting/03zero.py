#zero shot prompting : directly  giving the instruction to the model without any examples
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

SYSTEM_PROMPT = "You should only answer related to maths questions. If the question is not related to coding, just say sorry."
response = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "hii , what is  2+2?"}
    ]
)

print(response.choices[0].message.content)