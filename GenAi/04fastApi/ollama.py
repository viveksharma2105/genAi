from fastapi import FastAPI, Body
from ollama import Client
app = FastAPI()
client = Client(
    host="http://localhost:11434/ollama-server-running-on-this-host",
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/contact")
def read_contact():
    return {"Contact": "vivek@gmail.com"}

@app.post("/chat")
def chat(
    message: str = Body(..., description="The message to send to the model")
):
    response = client.chat(
        model="gemma:2b",
        messages=[
            {"role": "user", "content": message}
        ]
    )
    return {"response": response.message.content}

#download ollama inside docker and run ollama server in local and then run this code to test the api.