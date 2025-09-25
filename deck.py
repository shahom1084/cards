import random
class Carddeck:
    def __init__(self):
        self.cards = []
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    def create_deck(self):
        self.cards = [(rank, suit) for suit in self.suits for rank in self.ranks]
        return self.cards
    def shuffle_deck(self):
        random.shuffle(self.cards)
        return self.cards

deck = Carddeck()
deck.create_deck()
cards=deck.shuffle_deck()
print(cards)