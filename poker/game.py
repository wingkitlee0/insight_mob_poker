import random

from .poker import Card

class Game:
    def __init__(self):
        card = Card("")
        self.rank2chr = {v:k for k, v in card.card_dict.items()}
        self.suit2chr = ['C', 'D', 'H', 'S']

    def get_single_card(self):
        rank = self.rank2chr[random.randint(2,14)]
        suit = self.suit2chr[random.randint(0,3)]
        return rank+suit

    def get_a_hand(self):
        """
        generate a hand of 5 cards without duplicates
        """
        hand = set()
        while len(hand) < 5:
            rank = self.rank2chr[random.randint(2,14)]
            suit = self.suit2chr[random.randint(0,3)]
            card = rank+suit
            if card not in hand:
                hand.add(card)
        return " ".join(list(hand))

    def get_two_hands(self):
        """
        generate two hands for a game (10 cards)
        """
        hand = set()
        while len(hand) < 10:
            rank = self.rank2chr[random.randint(2,14)]
            suit = self.suit2chr[random.randint(0,3)]
            card = rank+suit
            if card not in hand:
                hand.add(card)
        return " ".join(list(hand)[::2]), " ".join(list(hand)[1::2])


if __name__ == '__main__':
    game = Game()
