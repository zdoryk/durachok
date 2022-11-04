import player
from card import Card


class BotPlayer:  # TODO: дописать бота
    def __init__(self, trump: str):
        self.__hand = []
        self.__trump = trump
        self.has_turn: bool = False

    def print_hand(self) -> str:
        hand_str = '| '

        for card_ in self.__hand:
            hand_str += card_.get_full_info() + ' | '

        return hand_str

    def set_turn(self, state):
        self.has_turn = state

    def take_card(self, card: Card):
        self.__hand.append(card.set_position(11))

    def get_hand_size(self):
        return len(self.__hand)

    def defence(self, card):
        card = self.look_for_higher_than(card)
        print(card)
        return card

    def look_for_higher_than(self, card):
        possible_card = [card_ for card_ in self.__hand if card_.get_card_value() > card.get_card_value()
                         and card_.get_suit() == card.get_suit()]

        if len(possible_card) == 0 and card.suit != self.__trump:
            possible_card.extend([card_ for card_ in self.__hand if card_.suit == self.__trump])

        if len(possible_card) == 0:
            return 0
        else:
            # print(possible_card)
            card_ = sorted(possible_card, key=lambda c: c.get_card_value())[0]
            self.__hand.remove(card_)
            return card_

    def start_attack(self):
        possible_card = [card_ for card_ in self.__hand if card_.suit != self.__trump]

        if len(possible_card) == 0:
            possible_card.extend(self.__hand)

        card_ = sorted(possible_card, key=lambda c: c.get_card_value())[0]
        self.__hand.remove(card_)
        return card_

    def get_hand(self):
        return self.__hand
