# Card value
C6 = 6
C7 = 7
C8 = 8
C9 = 9
C10 = 10
J = 11
Q = 12
K = 13
A = 14
DECK_SIZE = 36


def rank_decompiler(int_value):
    if int_value == 6:
        return '6'

    if int_value == 7:
        return '7'

    if int_value == 8:
        return '8'

    if int_value == 9:
        return '9'

    if int_value == 10:
        return '10'

    if int_value == 11:
        return 'J'

    if int_value == 12:
        return 'Q'

    if int_value == 13:
        return 'K'

    if int_value == 14:
        return 'A'


class Card:
    def __init__(self, rank: str, suit: str, position: int):
        self.rank = rank
        self.suit = suit
        self.position = position  # REST solution
        self.card_index = 0

    def get_card_info(self) -> str:
        return f'{self.rank} of {self.suit}'

    def get_card_value(self) -> int:
        if self.rank == '6':
            return C6
        if self.rank == '7':
            return C7
        if self.rank == '8':
            return C8
        if self.rank == '9':
            return C9
        if self.rank == '10':
            return C10
        if self.rank == 'J':
            return J
        if self.rank == 'Q':
            return Q
        if self.rank == 'K':
            return K
        if self.rank == 'A':
            return A

    def set_position(self, pos: int):
        self.position = pos
        return self

    def get_suit(self):
        return self.suit

    def get_full_info(self):
        return f'{self.rank} of {self.suit} [{self.position}]'

    def get_card_dict(self):
        return {
            "card_rank": self.get_card_value(),
            "card_suit": self.suit.lower(),
            "card_height": 120,
            "card_index": self.card_index
        }


