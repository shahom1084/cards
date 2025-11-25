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
        self.player_ids = list(self.players.keys())
        self.dealer_index = 0 
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
    def end_round(self):
        if self.current_cards == 1:
            self.deal_direction = 1
        self.current_cards += self.deal_direction
        if self.current_cards > self.start_cards:
            self.current_cards = self.start_cards
            self.deal_direction = -1
        self.round_number += 1 
        self.dealer_index  = (self.dealer_index + 1) % len(self.player_ids)
        return True
    def calls(self):
        total_calls = 0
        call_order = self.player_ids[self.dealer_index + 1:] + self.player_ids[:self.dealer_index + 1]
        print(f"\n--- Round {self.round_number + 1}: Calling Hands ---")
        print(f"Dealer is Player {self.player_ids[self.dealer_index]}")
        print(f"Cards dealt this round: {self.current_cards}\n")
        for i, player_id in enumerate(call_order):   
            is_dealer = (i == len(call_order) - 1)
            while True:
                try: 
                    call = int(input(f"{self.players[player_id]['player_name']} enter your call "))
                    if not (0<= call <= self.current_cards):
                        print(f"Not a valid call Please enter a number between 0 and {self.current_cards}. ")
                        continue
                    if is_dealer:
                        forbidden_call= self.current_cards - total_calls
                        if call == forbidden_call:
                            print("Uh Oh!! you cannot call this number which sums up to the total number of hands")
                            continue
                    
                    self.players[player_id]['no_of_hands']=call
                    total_calls += call
                    break
                except ValueError:
                    print("Only Integer allowed")
        for player_id in self.player_ids:
            print(f"Player {player_id}: {self.players[player_id]['no_of_hands']} hands")
            



    def check_constrain_call(self,dist_id):
        self.admin_id =dist_id
        return dist_id
    def curr_round(self,players):
        self.players = players

    def curr_turn(self):
        curr_turn = super().curr_turn()
        return curr_turn

