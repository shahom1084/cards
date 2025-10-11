from game_state import game_state
from deck import CardDeck
from enum import Enum
class heirarchy(Enum):
    TRIO = 6
    STRAIGHT_FLUSH = 5
    STRAIGHT = 4
    FLUSH = 3
    PAIR = 2
    HIGH_CARD = 1

class TeenPatti(game_state):
    # rank_order = {rank: i for i, rank in enumerate(CardDeck().ranks)}
    def curr_turn(self):
        curr_turn = super().curr_turn()
        return curr_turn
    # def get_rank_index(self,player_id):
    #     card = self.players[player_id]['cards'][0]
    #     return CardDeck.ranks.index(card[0])
    def evaluate_hands(self,cards):
        sorted_cards=sorted(cards, key=lambda card: CardDeck().get_rank_value(card[0]))

        hand_rank=None
        if cards[0][0]==cards[1][0] and cards[1][0]==cards[2][0] and cards[1][0]==cards[2][0]:
            hand_rank = heirarchy.TRIO.value
        return (hand_rank,sorted_cards)

        
        
        
            





        

    # @staticmethod
    def rules(self,players):
        curr_winner = next(iter(players))
        for pid,data in players.items():
            pass
        
            

