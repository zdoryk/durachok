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

class Card:
    def __init__(self, rank: str, suit: str, position: int):
        self.rank = rank
        self.suit = suit
        self.position = position  # REST solution

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

    def get_full_info(self):
        return f'{self.rank} of {self.suit} [{self.position}]'

