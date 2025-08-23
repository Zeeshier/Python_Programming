from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatModel(BaseModel):
    message : str

@app.post("/chat")
def chat(data : ChatModel):
    print("[+] data received " , data)
    return {"message" : "Data Validation with Pydantic"}