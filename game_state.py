from dataclasses import dataclass
from game import Game
from deck import CardDeck
from typing import Optional
# @dataclass
class game_state(Game):
    def __init__(self, game: Game, no_of_players: int):
        # manually copy parent fields
        self.game_id = game.game_id
        self.game_name = game.game_name
        self.no_of_cards = game.no_of_cards
        self.players = game.players
        self.max_no_of_players = game.max_no_of_players
        self.no_of_players = no_of_players
        self.player_ids = list(self.players.keys())
        self.turn_index = 0

    # @classmethod
    # def from_game(cls, game: Game, no_of_players):
        
    #     return cls(
    #         game_id=game.game_id,
    #         game_name=game.game_name,
    #         no_of_cards=game.no_of_cards,
    #         players=game.players,
    #         max_no_of_players=game.max_no_of_players,
    #         no_of_players=no_of_players
    #     )

    def set_no_of_players(self):
        if self.no_of_players is None or self.max_no_of_players is None:
                return "No. of players required"
            
        if self.no_of_players is None:
            self.no_of_players=self.max_no_of_players

    def distribute_cards(self,deck,players):
        self.deck = deck
        self.set_no_of_players()
        self.players=players
        print(f"Distributing cards to {self.no_of_players} players ")
        for _ in range(self.no_of_cards):
            for player_id in self.players:
                if deck:
                    if 'cards' not in self.players[player_id]:
                        self.players[player_id]['cards'] = []
                    self.players[player_id]['cards'].append(CardDeck.draw_card(deck))
        
        return self.players
        
    def curr_turn(self):
        current_player = self.player_ids[self.turn_index % len(self.player_ids)]
        self.turn_index += 1
        return current_player


            
        
        