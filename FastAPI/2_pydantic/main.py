from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MessageInput(BaseModel):
    role : str
    content : str

class ChatModel(BaseModel):
    messages : list[MessageInput]

@app.post("/chat")
def chat(data : ChatModel):
    print("[+] ChatInput Type: " , type(data.model_dump()))
    print("[+] ChatInput: " , data)
    print("[+] Messages Type: " , type(data.messages))
    print("[+] Messages: " , data.messages)


    return {"message" : "Data Validation with Pydantic"}