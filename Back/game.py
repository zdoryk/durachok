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
        # Game setup :
        self.__deck = Deck()
        self.__table = Table()
        self.__discard = []
        self.__trump = self.__deck.get_trump()

        # Players :
        self.__player = Player(self.__trump)
        self.__bot_player = BotPlayer(self.__trump)

        self.__create_game()

    def __create_game(self):
        for i in range(6):
            self.__player.take_card(self.__deck.get_card())
            self.__bot_player.take_card((self.__deck.get_card()))


    # def test(self):
    #     self.__deck.get_card()
        
    def get_initial(self):
        return {
            "player_cards": self.return_player().get_hand(),
            "trump": self.get_trump(),
            "player_state": self.__player.has_turn,
            "deck_size": self.get_deck_size()
        }
    
    # TODO: Доделать козырь
    def get_trump(self):
        # return self.__trump
        return self.__deck.get_last_card().get_card_dict()

    def return_player(self):
        return self.__player

    def get_deck_size(self) -> int:
        return self.__deck.get_deck_size()

    def return_discard(self):
        return self.__discard

    def start_game(self):  # TODO: подумать о реализации подбрасывания карт
        self.__choose_first_one()
        
        # Играется до моментка пока у одного из игроков не останется карт
        while self.__player.get_hand_size() != 0 and self.__bot_player.get_hand_size() != 0:
            self.__lead()

            if self.__player.get_hand_size() == 0:
                print("player won")

            if self.__bot_player.get_hand_size() == 0:
                print("bot won")

    def __take_cards(self, turn_status):
        player_need = 6 - self.__player.get_hand_size()
        bot_need = 6 - self.__bot_player.get_hand_size()

        if turn_status == 1:
            self.__take_card_from_deck(self.__bot_player, bot_need)

        if turn_status == 2:
            self.__take_card_from_deck(self.__player, player_need)

        if turn_status == 0:
            if self.__player.has_turn:
                self.__take_card_from_deck(self.__bot_player, bot_need)
                self.__take_card_from_deck(self.__player, player_need)

            else:
                self.__take_card_from_deck(self.__player, player_need)
                self.__take_card_from_deck(self.__bot_player, bot_need)

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

        self.__take_cards(turn_status)

    def __choose_first_one(self):
        self.__player.set_turn(1)
        player_trump_cards = [card_ for card_ in self.__player.get_hand() if card_.suit == self.__trump]
        bot_trump_cards = [card_ for card_ in self.__bot_player.get_hand() if card_.suit == self.__trump]
        sorted(player_trump_cards, key=lambda card_: card_.get_card_value())
        sorted(bot_trump_cards, key=lambda card_: card_.get_card_value())

        if len(player_trump_cards) == 0 and len(bot_trump_cards) == 0:
            pass

        if len(player_trump_cards) == 0 and len(bot_trump_cards) > 0:
            self.__give_turn()

        if len(player_trump_cards) > 0 and len(bot_trump_cards) > 0:
            if bot_trump_cards[0].get_card_value() < player_trump_cards[0].get_card_value():
                self.__give_turn()

        if self.__player.has_turn:
            print("Player starts")

        if self.__bot_player.has_turn:
            print("Bot starts")

    def __lead(self):
        # Часть игрока
        if self.__player.has_turn:
            # Выбираем карту
            player_decision = self.__player.start_attack(self.__table.return_cards())

            # Написано на случай, если игрок не захочет подкидывать карту.
            if not player_decision or self.__player.get_hand_size() == 0:
                self.__end_turn(0)
                self.__give_turn()

            else:
                # Кладём карту на стол
                self.__table.new_attack(player_decision)
                # Просим бота сделать решение
                card_ = self.__bot_player.defence(self.__table.return_card_for_beat())

                # Если у него есть карта, которой он может побиться то :
                if card_:
                    print(f"Bot beats using {card_.get_card_info()}")
                    self.__table.beat_card(card_)
                    # self.__end_turn(0)
                    # self.__give_turn()
                    self.__lead()
                else:
                    self.__end_turn(2)

        # Часть бота
        if self.__bot_player.has_turn:
            # бот походил
            card_ = self.__bot_player.start_attack(self.__table.return_cards())

            # на те случаи, когда бот должен подкинуть, но не может
            if not card_:
                self.__end_turn(0)
                self.__give_turn()

            if card_:
                # Карта появилась на столе
                self.__table.new_attack(card_)

                # Игрок выбирает карту, который он будет биться
                player_card = self.__player.defend(self.__table.return_card_for_beat())

                # Если игрок таки решил побиться
                if player_card:
                    self.__table.beat_card(player_card)
                    self.__lead()
                # Если игрок не бьется, то он забирает карты
                else:
                    self.__end_turn(1)

    # Передача хода другому игроку
    def __give_turn(self):

        if self.__player.has_turn:
            self.__player.set_turn(0)
            self.__bot_player.set_turn(1)

        else:
            self.__player.set_turn(1)
            self.__bot_player.set_turn(0)

    def __take_card_from_deck(self, player, amount_of_cards):
        if amount_of_cards > 0:
            for i in range(amount_of_cards):
                if self.__deck.get_deck_size() == 0:
                    break
                player.take_card(self.__deck.get_card())
