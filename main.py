from fastapi import FastAPI
from enum import Enum

class Players(str, Enum):
    Stafford = "Stafford"
    Mahomes = "Mahomes"
    Brady = "Brady"
    Manning = "Manning"

app = FastAPI()

@app.get("/players/{my_players}")
async def get_players(my_players:Players):
    if my_players == Players.Stafford:
        return{"players_name":my_players.value, "message": "You are a superbowl winning quarterback. "}

    if my_players == Players.Mahomes:
        return {"players_name" : my_players.value, "message" : "You're a young Legend! "}
   
    if my_players == Players.Brady:
        return{"players_name":my_players.value, "message": "You're the GOAT!"}
    
    if my_players == Players.Manning:
        return{"players_name":my_players.value, "message" : "You're a funny dude"}
