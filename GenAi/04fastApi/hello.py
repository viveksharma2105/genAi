from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/contact")
def read_contact():
    return {"Contact": "vivek@gmail.com"}