from card import Card


class Table:
    def __init__(self):
        self.__table = []

    def beat_card(self, card: Card):
        card.card_index = len(self.__table)
        self.__table[-1].append(card)

    def new_attack(self, card_: Card):
        card_.set_position(1)
        self.__table.append([card_])
        card_.card_index = len(self.__table)

    def return_cards(self) -> [Card]:
        return [card for pair in self.__table for card in pair]

    def clear_table(self):
        self.__table = []

    def return_card_for_beat(self):
        return self.__table[-1][0]
