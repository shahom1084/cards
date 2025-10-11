from dataclasses import dataclass, field
import random

@dataclass
class CardDeck:
    suits: list[str] = field(default_factory=lambda: ['Hearts','Diamonds','Clubs','Spades'])    
    ranks: list[str] =  field(default_factory=lambda: ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace'])
    cards: list[tuple[str, str]] = field(default_factory=list)

    def create_deck(self):
        self.cards = [(rank, suit) for suit in self.suits for rank in self.ranks]
        return self.cards

    def shuffle_deck(self):
        random.shuffle(self.cards)
        return self.cards
    @staticmethod
    def draw_card(deck):
        
        return deck.pop() if deck else None
