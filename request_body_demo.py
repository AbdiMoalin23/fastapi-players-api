from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str 
    height: float | None = None
    net: int | None = None
    team: str

app = FastAPI()

fake_db = []

@app.post("/items/")
async def create_item(item: Item):
    fake_db.append(item.model_dump())
    return {"message":"item saved"}

@app.get("/items/")
async def get_items():
    return fake_db