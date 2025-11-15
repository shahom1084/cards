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
    def __init__(self, game, num_players,pot_value):
        super().__init__(game, num_players)
        self.pot_value = pot_value
        for player_id in self.players:
            self.players[player_id]['has_packed'] = False
            self.players[player_id]['is_seen'] = False
        print(self.players)
    # rank_order = {rank: i for i, rank in enumerate(CardDeck().ranks)}
    def pack_player(self,player_id):
        self.players[player_id]['has_packed'] = True
        
    def see_cards(self,player_id):
        self.players[player_id]['has_packed'] = True
    


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
        elif  sorted_cards[0][0] == sorted_cards[1][0] or sorted_cards[1][0] == sorted_cards[2][0]:
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
        # idhar se likhna hai for equal ranks
        remain_players=list(range(len(curr_game_state)))
        if curr_game_state[0][0]==curr_game_state[1][0]:
            for i in range(2,-1,-1):
                max_cards=[CardDeck().get_rank_value(curr_game_state[j][1][i][0]) for j in remain_players]
                curr_winner = max(max_cards)
                remain_players=[remain_players[i] for i,v in enumerate(max_cards) if v==curr_winner]
                if len(remain_players)==1:
                    winner_index=remain_players[0]
                    winner = curr_game_state[winner_index][2]
                    break

        return winner
        

class TeenPattiMoves(TeenPatti):
#    print(self.players)
    def chaal(self,player_id,bet_amount):
        self.player_id=player_id
        self.bet_amount = self.pot_value * 2
        if self.players[player_id]['is_seen'] == True:
            self.players[player_id]['money'] -=  bet_amount
        else:
            return "You can't play chaal without seeing your cards."
        
    def blind(self,player_id,bet_amount):
        self.player_id = player_id
        self.bet_amount = self.pot_value
        if self.players[player_id]['is_seen'] == True:
            return "you can't play blind"
        else:
            self.players[player_id]['money'] -=  bet_amount

    def pack(self,player_id):
        self.player_id = player_id
        if self.players[player_id]['has_packed'] == False:
            self.players[player_id]['has_packed'] = True



    def raise_pot(self,raise_amount):
        self.pot_value+=raise_amount



