from deck import Deck
from table import Table
from player import Player
from bot_player import BotPlayer


# Deck.pos = 0
# Table.pos = 1
# Discard.pos = -1
# Turns status: player takes = 1, bot takes = 2, discard = 0


class Game:
    def __init__(self):
        self.__player = Player()
        self.__bot_player = BotPlayer()
        self.__deck = Deck()
        self.__table = Table()
        self.__discard = []

        self.__create_game()

    def __create_game(self):
        for i in range(6):
            self.__player.take_card(self.__deck.get_card())
            self.__bot_player.take_card((self.__deck.get_card()))

    def return_players(self):
        return self.__player, self.__bot_player

    def get_deck_size(self) -> int:
        return self.__deck.get_deck_size()

    def return_discard(self):
        return self.__discard

    def start_game(self):  # TODO: подумать о реализации подбрасывания карт
        while self.__player.get_hand_size() != 0 and self.__bot_player.get_hand_size() != 0:
            self.__table.new_attack(self.__player.start_attack())
            # bot`s move
            # if ....
            # ...
            self.__end_turn(0)
            print(self.__discard)

    def __take_cards(self):  # TODO: создать поочередность взятия карт в зависимости от того, кто ходил
        player_need = 6 - self.__player.get_hand_size()
        bot_need = 6 - self.__bot_player.get_hand_size()

        if player_need > 0:
            for i in range(player_need):
                if self.__deck.get_deck_size() == 0:
                    break
                self.__player.take_card(self.__deck.get_card())

        if bot_need > 0:
            for i in range(bot_need):
                if self.__deck.get_deck_size() == 0:
                    break
                self.__bot_player.take_card(self.__deck.get_card())

    def __end_turn(self, turn_status):
        if turn_status == 0:
            cards = self.__table.return_cards()
            cards = [card_.set_position(-1) for card_ in cards]
            # for card_ in cards:
            #     card_.set_position(-1)
            self.__discard.extend(cards)

        if turn_status == 1:
            for card_ in self.__table.return_cards():
                self.__player.take_card(card_)

        if turn_status == 2:
            for card_ in self.__table.return_cards():
                self.__bot_player.take_card(card_)

        self.__table.clear_table()

        self.__take_cards()
