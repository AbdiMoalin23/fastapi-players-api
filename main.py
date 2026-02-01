from fastapi import FastAPI
from enum import Enum

class Players(str, Enum):
    Stafford = "Stafford"
    Mahomes = "Mahomes"
    Brady = "Brady"
    Manning = "Manning"

app = FastAPI()

@app.get("/players/{my_players}")
async def get_players(my_players:Players, short: bool = False):

    base_response = {
        "player_name" : my_players.value
    }
    #if short = true, return only the name
    if short:
        return base_response
    #otherwise, return name + message
    if my_players == Players.Stafford:
        message = "You are a superbowl winning Quarterback!"
    elif my_players == Players.Mahomes:
        message = "You are a young Legend!"
    elif my_players == Players.Brady:
        message = "You are the GOAT!"
    else: #Manning
        message = "You are a funny dude."
    
    base_response["message"] = message
    return base_response
        
    
