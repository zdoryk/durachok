import player
from card import Card


class BotPlayer:  # TODO: дописать бота
    def __init__(self):
        self.__hand = []

    def get_hand(self) -> str:
        hand_str = '| '

        for card_ in self.__hand:
            hand_str += card_.get_full_info() + ' | '

        return hand_str

    def take_card(self, card: Card):
        # card.set_position(11)
        self.__hand.append(card.set_position(11))

    def get_hand_size(self):
        return len(self.__hand)
