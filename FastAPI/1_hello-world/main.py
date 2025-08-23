from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"Message" : "Hello World"}

@app.post("/chat")
def chat(messages : dict):
    print("Data Received : ", messages) 
    return messages