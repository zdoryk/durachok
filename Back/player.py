from card import Card, DECK_SIZE


class Player:
    def __init__(self, trump: str):
        self.__hand = []
        self.__trump = trump
        self.has_turn: bool = False

    def take_card(self, card: Card):
        # card.set_position(10)
        self.__hand.append(card.set_position(11))

    def print_hand(self) -> str:
        hand_str = ''

        for i in range(len(self.__hand)):
            hand_str += f'{i} - {self.__hand[i].get_card_info()} \n'

        return hand_str

    def get_hand_size(self) -> int:
        return len(self.__hand)

    def start_attack(self):
        print('Player`s turn')
        print(f"Trump : {self.__trump}")
        print(self.print_hand())
        choose = DECK_SIZE + 1
        while int(choose) >= self.get_hand_size() or int(choose) == -1:
            choose = int(input('Choose a card -> '))

        return self.__hand.pop(choose)

    def set_turn(self, state):
        self.has_turn = state

    def defend(self, card_):
        if self.__can_i_beat_it(card_):
            choose = DECK_SIZE + 1
            #while int(choose) >= self.get_hand_size() or int(choose) == -1:
            while True:
                print(f"Trump : {self.__trump}")
                print(f"Card for beating : {card_.get_card_info()}")
                print(self.print_hand())

                choose = int(input('Choose a card -> '))

                if int(choose) == -1:
                    return False

                if self.__hand[choose].get_card_value() > card_.get_card_value() and \
                        self.__hand[choose].suit == card_.suit:
                    break

                if self.__hand[choose].suit == self.__trump and card_.suit != self.__trump:
                    break

                else:
                    print("You cannot beat using this card")

            return self.__hand.pop(choose)

        else:
            return False

    def surrender(self):
        pass

    def __can_i_beat_it(self, card_for_beating):
        possible_card = [card_ for card_ in self.__hand if
                         card_.get_card_value() > card_for_beating.get_card_value()
                         and card_.get_suit() == card_for_beating.get_suit()]

        if len(possible_card) == 0 and card_for_beating.suit != self.__trump:
            possible_card.extend([card_ for card_ in self.__hand if card_.suit == self.__trump])

        if len(possible_card) == 0:
            return False
        else:
            return True

    def get_hand(self):
        return self.__hand
