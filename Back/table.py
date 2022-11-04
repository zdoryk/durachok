from card import Card


class Table:
    def __init__(self):
        self.__table = []

    def beat_card(self, card: Card):
        self.__table[-1].append(card)

    def new_attack(self, card: Card):
        card.set_position(1)
        self.__table.append([card])

    def return_cards(self) -> [Card]:
        return [card for i in self.__table for card in i]

    def clear_table(self):
        self.__table = []

    def return_card_for_beat(self):
        return self.__table[-1][0]
