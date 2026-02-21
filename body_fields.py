from fastapi import FastAPI, Body, Path
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()
fake_db = []

class User(BaseModel):
    first_name : str = Field( min_length=2 )
    last_name : str = Field( min_length=2 )
    age : int | None = Field( default=None, gt=0, title="The age of the user" )


class Info(BaseModel):
    role : str
    salary : float | None = Field( default=None, gt=0, description="The Salary must be greater than 0" )
    experience : int = Field( ge=0 )

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