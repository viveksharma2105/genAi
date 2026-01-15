from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
clint = OpenAI()

response = clint.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {"role": "system", "content": "You are expert in Mathematics.If the query is not related to Mathematics, politely refuse to answer"},
        {"role": "user", "content": "hii , what is  you name?"}
    ]
)


print(response.choices[0].message.content)