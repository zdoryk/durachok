import card
from random import shuffle


class Deck:
    def __init__(self):
        self.__deck = []

        self.__create_deck()

    def __create_deck(self):
        for suit in ['Diamonds', 'Hearts', 'Clubs', 'Spades']:
            for rank in ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                self.__deck.append(card.Card(rank, suit, 0))

        shuffle(self.__deck)

    def get_deck(self):
        return self.__deck

    def get_str_deck(self):
        deck_str = ''

        for card_ in self.__deck:
            deck_str += card_.get_card_info() + '\n'

        return deck_str

    def get_card(self):
        return self.__deck.pop(0)

    def get_deck_size(self):
        return len(self.__deck)

