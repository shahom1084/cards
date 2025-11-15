from game_state import game_state
from deck import CardDeck

class kachuFul(game_state):
    TRUMP_ORDER = ['Spades','Diamonds','Clubs','Hearts']
    def __init__(self, game, no_of_players):
        super().__init__(game, no_of_players)
        self.round_number = 0
        self.trump_suit =None
        self.start_cards = 52 // no_of_players
        self.current_cards = self.start_cards 
        self.deal_direction = -1
        
        for player_id in self.players:
            self.players[player_id]['no_of_hands']=0
            self.players[player_id]['hands_scored']=-1
            self.players[player_id]['total_score'] = 0

    #method overrided due to different method of distributing card
    
    def distribute_cards(self, deck, players):
        self.deck = deck 
        self.players = players
        for _ in range(self.current_cards):
            for player_id in self.players:
                if deck:
                    if 'cards' not in self.players[player_id]:
                        self.players[player_id]['cards'] = []
                    if _ == 0: 
                       self.players[player_id]['cards'] = []
                    card = CardDeck.draw_card(deck)
                    if card:
                        self.players[player_id]['cards'].append(card)
        return self.players
    def prepare_round(self,deck):
        self.trump_suit = self.TRUMP_ORDER[self.round_number % 4]
        print(f"Trump : {self.trump_suit} \n")
        self.distribute_cards(deck,self.players)
    # def calls(self,player_id,no_of_hands):
    #     self.no_of_hands=no_of_hands
    #     self.player_id=player_id
    #     self.players[player_id]['no_of_hands']=no_of_hands

    def curr_turn(self):
        curr_turn = super().curr_turn()
        return curr_turn

