from fastapi import FastAPI, Body, Path
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()
fake_db = []

class User(BaseModel):
    first_name : str
    last_name : str 
    age : float | None = None


class Info(BaseModel):
    role : str
    salary : float | None = None
    experience : int

@app.put("/items/{item_id}/")
async def update_user(
    item_id : Annotated[int, Path(title="ID of the user")],
    confidential : Annotated[int, Body()],
    user : User | None = None,
    info : Info | None = None,
    q : str | None = None , 
 ):
    fake_db.append({
        "item_id" : item_id,
        "confidential" : confidential,
        "user" : user.model_dump() if user else None,
        "info" : info.model_dump() if info  else None,
        "q" : q, 

    })
    return{"message":"item saved"}

@app.get("/items/{user_id}/")
async def get_user(user_id : int):
    for item in fake_db:        
        if item["item_id"] == user_id:
            return item
    return{"error" : "not found"}
