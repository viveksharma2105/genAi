from openai import OpenAI
from dotenv import load_dotenv
import requests

load_dotenv()

client = OpenAI()


def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    
    if response.status_code == 200:
        return f"The current weather in {city} is: {response.text}"
    return "Sorry, I couldn't fetch the weather information right now."


def main():
    user_query = input(">")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": user_query}
        ]
    )
    
    print(f"🤖:{response.choices[0].message.content}")
    
main()