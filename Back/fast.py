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
        return {"status": "OK", "data": our_game.get_world_info()}
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


@app.post("/player_card")
async def player_card(p_card: PlayerCard):
    try:
        # Если игрок начинает ход / подбрасывает
        if our_game.return_player().has_turn:
            # Предполагаю, что кнопка завершить ход будет недоступна, если игрок обязан походить
            # Для тех случаев, когда игрок уже походил и бот побился
            if int(p_card.dict()['card_rank']) == -1:
                data = our_game.lead_player_side(False)
                return {"Status": "200 OK", "data": data}

            else:
                card_ = [rank_decompiler(int(p_card.dict()['card_rank'])), p_card.dict()['card_suit']]

                print(card_)

                # Бот выбрал карту
                bot_card = our_game.lead_player_side(card_)

                print(f"bot card : {bot_card}")

                print(type(bot_card))

                # Если бот выбрал бить карту на столе
                if bot_card:
                    return {"Status": "200 OK", "bot_card": f"{bot_card.get_card_dict()}"}

                # Бот решил забрать карты на столе
                if not bot_card:
                    our_game.end_turn(2)
                    return {"Status": "200 OK", "bot_card": "-1"}

        # Если игрок защищается
        if not our_game.return_player().has_turn:
            # Игрок решил побить карту на столе
            if int(p_card.dict()['card_rank']) != -1:
                card_ = [rank_decompiler(int(p_card.dict()['card_rank'])), p_card.dict()['card_suit']]

                # Либо получим передачу хода, либо новую карту от бота | Мы всегда получаем словарь на выходе
                decision = our_game.lead_bot_side(1, card_)

                # Если бот прекратил подбрасывать
                if "bot_hand_size" in decision.keys():
                    return {"Status": "200 OK", "data": decision}

                if "card_suit" in decision.keys():
                    return {"Status": "200 OK", "bot_card": decision}

            # Игрок решил забрать забрать карты на столе /  На свой ответ он получет
            if int(p_card.dict()['card_rank']) == -1:
                decision = our_game.lead_bot_side(-1)
                return {"Status": "200 OK", "data": f"{our_game.get_world_info()}", "bot_card": decision}

    except Exception as e:
        return e


@app.get("/get_table")
async def get_table():
    cards = [card_.get_card_dict() for card_ in our_game.return_table()]
    data = {
        "cards_on_bot": [cards[i] for i in range(len(cards)) if i % 2 == 0],
        "cards_on_top": [cards[i] for i in range(len(cards)) if i % 2 == 1]
    }
    return {"Status": "200 OK", "cards": data}
