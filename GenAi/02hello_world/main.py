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



##By using Google Gemini API Key
# from openai import OpenAI
# clint = OpenAI(
#     api_key="YOUR_GOOGLE_GEMINI_API_KEY",
#     base_url="https://generativelanguage.googleapis.com/v1beta/"
    
# )

# response = clint.chat.completions.create(
#     model="gemini-2.5-flash",
#     messages=[
#         {"role": "user", "content":"Hey  there!"}
#     ]
# )

# print(response.choices[0].message.content)