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
        #TRIO checking
        if cards[0][0]==cards[1][0] and cards[1][0]==cards[2][0] and cards[1][0]==cards[2][0]:
            hand_rank = heirarchy.TRIO.value
        elif int( CardDeck().get_rank_value(sorted_cards[0][0]))-int(CardDeck().get_rank_value(sorted_cards[1][0]))==-1 and int(CardDeck().get_rank_value(sorted_cards[1][0]))-int(CardDeck().get_rank_value(sorted_cards[2][0]))==-1 :
            hand_rank = heirarchy.STRAIGHT.value #unpure sequence 
            if sorted_cards[0][1]==sorted_cards[1][1] and sorted_cards[1][1]==sorted_cards[2][1]:
                hand_rank = heirarchy.STRAIGHT_FLUSH.value #pure sequence
        #color 
        elif sorted_cards[0][1]==sorted_cards[1][1] and sorted_cards[1][1]==sorted_cards[2][1]:
            hand_rank = heirarchy.FLUSH.value #color
        #pair 
        elif sorted_cards[0][0]==sorted_cards[1][0]:
            hand_rank = heirarchy.PAIR.value #PAIR
        #high-card
        else:
            hand_rank = heirarchy.HIGH_CARD.value #high card



        return (hand_rank,sorted_cards)


        
        
        
            





        

    # @staticmethod
    def rules(self,players):
        winner = next(iter(players))
        curr_game_state=[]
        for pid,data in players.items():
            cards = data['cards'] 
            hand_rank,sorted_cards=self.evaluate_hands(cards)
            curr_game_state.append((hand_rank,sorted_cards,pid))
        curr_game_state.sort(key=lambda x:x[0],reverse=True)
        #ALl three different  ranks 
        if curr_game_state[0][0]!=curr_game_state[1][0]:
            winner = curr_game_state[0][2]
        return winner
        

    

        
        
            

