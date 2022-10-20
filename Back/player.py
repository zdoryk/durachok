from card import Card, DECK_SIZE


class Player:
    def __init__(self):
        self.__hand = []

    def take_card(self, card: Card):
        # card.set_position(10)
        self.__hand.append(card.set_position(11))



    def get_hand(self) -> str:
        hand_str = ''

        for i in range(len(self.__hand)):
            hand_str += f'{i} - {self.__hand[i].get_card_info()} \n'

        return hand_str

    def get_hand_size(self):
        return len(self.__hand)

    def start_attack(self):
        print(self.get_hand())
        choose = DECK_SIZE + 1
        while int(choose) >= self.get_hand_size():
            choose = input('Choose a card -> ')

        return self.__hand.pop(int(choose))

    def defend(self):
        pass

    def surrender(self):
        pass

    def stop_attack(self):
        pass

