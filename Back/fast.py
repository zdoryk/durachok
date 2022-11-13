from fastapi import FastAPI
import json
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from game import Game
from card import rank_decompiler

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


@app.get("/get_player_hand")
async def get_player_hand():
    try:
        return our_game.return_player_hand()

    except Exception as e:
        return e


class PlayerCard(BaseModel):
    card_rank: int
    card_suit: str

#
@app.post("/player_card")
async def player_card(p_card: PlayerCard):
    try:
        card_ = [rank_decompiler(int(p_card.dict()['card_rank'])), p_card.dict()['card_suit']]

        bot_card = our_game.lead_player_side(card_)

        print(f"bot card : {bot_card}")

        print(type(bot_card))
#
        if bot_card:
            return {"Status": "200 OK", "bot_card": f"{bot_card.get_card_dict()}"}

        if not bot_card:
            our_game.end_turn(2)
            return {"Status": "200 OK", "bot_card": "-1"}

    except Exception as e:
        return e
