from fastapi import FastAPI
import json
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from game import Game
our_game = Game()

# Create object of a class FastAPI
app = FastAPI()

# Pick origins wich can get data
# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
#     "http://localhost:*",
#     "http://localhost:3000"
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/initial")
async def start_game():
    try:
        return {"status": "OK", "data": our_game.get_initial()}
    except Exception as e:
        return e



class PlayerCard(BaseModel):
    card_rank: int
    card_suit: str


@app.post("/player_card")
async def player_card(player_card: PlayerCard):
    try:
        print(player_card.dict()['card_rank'])
        return {"Status": "200 OK"}
    except Exception as e:
        return e