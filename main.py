from deck import CardDeck
from players import Player
from game import Game
from game_state import game_state
from teen_patti import TeenPatti
deck = CardDeck()
game_deck= deck.create_deck()
shuffled_deck = deck.shuffle_deck()

p1 = Player(1,"om",500)
p2 = Player(2,"Raj",500)
p3 = Player(3,"xyz")

g1= Game(1,"Teen Patti",3,{p1.player_id:{"money":p1.money},p2.player_id:{"money":p2.money},p3.player_id:{"money":p3.money}})
# gs1= game_state(g1,no_of_players=3)
tp_game = TeenPatti(g1, num_players=3)
# print(gs1)
# hands=gs1.distribute_cards(shuffled_deck,g1.players)
hands = tp_game.distribute_cards(shuffled_deck, g1.players)
print(hands)
