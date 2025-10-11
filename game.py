from dataclasses import dataclass,field
from typing import Optional,Dict
from players import Player
@dataclass
class Game:
    game_id:int 
    game_name:str 
    no_of_cards:int

    players: Dict[int, dict] = field(default_factory=dict)
    max_no_of_players: Optional[int] = None

    def add_player(self,player_id):
        self.player_id=player_id
        self.players[player_id]={}

        return self.players
