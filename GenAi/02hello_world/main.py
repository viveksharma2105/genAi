from  dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
clint = OpenAI()

response = clint.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {"role": "user", "content":"Hey  there!"}
    ]
)

print(response.choices[0].message.content)