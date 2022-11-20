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

        self.__choose_first_one()

    def get_world_info(self):
        x = {
            "player_cards": self.return_player().get_hand(),
            "trump": self.get_trump(),
            "player_state": self.__player.has_turn,
            "deck_size": self.get_deck_size()
        }
        if self.__bot_player.has_turn:
            decision = self.lead_bot_side(0)
            x["bot_card"] = decision

        x["bot_hand_size"] = self.__bot_player.get_hand_size()

        return x

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

    def end_turn(self, turn_status):
        # Бито
        if turn_status == 0:
            cards = self.__table.return_cards()
            cards = [card_.set_position(-1) for card_ in cards]
            # for card_ in cards:
            #     card_.set_position(-1)
            self.__discard.extend(cards)

        # Игрок забирает карты на столе
        if turn_status == 1:
            for card_ in self.__table.return_cards():
                self.__player.take_card(card_)

        # Бот забирает карты на столе
        if turn_status == 2:
            for card_ in self.__table.return_cards():
                self.__bot_player.take_card(card_)

        # Чистим стол
        self.__table.clear_table()

        # Добираем карты из колоды, если на то есть нужда
        self.__take_cards(turn_status)

    def __choose_first_one(self):
        self.__player.set_turn(True)
        player_trump_cards = [card_ for card_ in self.__player.get_cards() if card_.suit == self.__trump]
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

    # Ограничение на выбор карты будет по стороне фронта
    def lead_player_side(self, player_decision):
        # Игрок ходит \ подбрасывает
        if player_decision:
            print('H1')
            player_card = self.__player.start_attack(player_decision)
            print(player_card.get_card_dict())
            self.__table.new_attack(player_card)
            print('H2')

            bot_card = self.__bot_player.defence(player_card)

            if bot_card:
                print('HB1')

                self.__table.beat_card(bot_card)
                print(bot_card.get_card_dict())

            return bot_card

        # Игрок прекращает подбрасывать
        if not player_decision:
            # Убираем карты в отбой
            self.end_turn(0)

            # Передаем ход боту
            self.__give_turn()
            self.lead_bot_side()

    def lead_bot_side(self, player_beat=0, p_card=[]):
        # Если игрок бьет карту бота / ограничение на выбор карты по стороне фронта
        if player_beat == 1:
            # Если игрок собирается бить карту, то переменная player_beat будет картой : Card
            player_card = self.__player.start_attack(p_card)

            self.__table.beat_card(player_card)

            # Перебрасываем на часть с подкидыванием бота
            player_beat = 0

        # Игрок решил забрать карты на столе
        if player_beat == -1:
            self.end_turn(1)
            # Предпологаю, что визуальная очистка стола будет по стороне веба
            self.lead_bot_side(0)

        # Бота начинает ход/подбрасывает
        if player_beat == 0:
            # бот походил
            card_ = self.__bot_player.start_attack(self.__table.return_cards())

            # на те случаи, когда бот должен подкинуть, но не может/ не хочет
            if not card_:
                self.end_turn(0)
                self.__give_turn()
                return self.get_world_info()

            if card_:
                # Карта появилась на столе
                self.__table.new_attack(card_)
                return card_.get_card_dict()

    def __lead(self):
        # Часть игрока
        if self.__player.has_turn:
            # Выбираем карту
            player_decision = self.__player.start_attack(self.__table.return_cards())

            # Написано на случай, если игрок не захочет подкидывать карту.
            if not player_decision or self.__player.get_hand_size() == 0:
                self.end_turn(0)
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
                    self.end_turn(2)

        # Часть бота
        if self.__bot_player.has_turn:
            # бот походил
            card_ = self.__bot_player.start_attack(self.__table.return_cards())

            # на те случаи, когда бот должен подкинуть, но не может
            if not card_:
                self.end_turn(0)
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
                    self.end_turn(1)

    # Передача хода другому игроку
    def __give_turn(self):

        if self.__player.has_turn:
            self.__player.set_turn(False)
            self.__bot_player.set_turn(True)

        else:
            self.__player.set_turn(True)
            self.__bot_player.set_turn(False)

    def __take_card_from_deck(self, player, amount_of_cards):
        if amount_of_cards > 0:
            for i in range(amount_of_cards):
                if self.__deck.get_deck_size() == 0:
                    break
                player.take_card(self.__deck.get_card())

    def return_player_hand(self):
        return self.return_player().get_hand()

    def return_table(self):
        return self.__table.return_cards()
