import unittest
from game import Game
from kachuful import kachuFul
from deck import CardDeck
from players import Player

class TestKachuful6Players(unittest.TestCase):

    def setUp(self):
        """
        This method now sets up a game with 6 players to test the division logic.
        """
        # 1. Setup 6 players
        players = [Player(i, f"Player {i}") for i in range(1, 7)]
        player_dict = {p.player_id: {} for p in players}

        # 2. Create the Game instance for Kachuful with 6 players
        kachuful_game_setup = Game(
            game_id=3,
            game_name="Kachuful-6p",
            no_of_cards=0,
            players=player_dict
        )

        # 3. Create the kachuFul game state
        self.game = kachuFul(kachuful_game_setup, no_of_players=6)
        
        # 4. Create a fresh, ordered deck for predictable testing
        self.deck = CardDeck().create_deck()

    def test_initialization_6_players(self):
        """
        Tests that __init__ calculates the correct starting card count for 6 players.
        """
        print("\n--- Testing __init__ (6 Players) ---")
        self.assertEqual(self.game.no_of_players, 6)
        self.assertEqual(self.game.round_number, 0)
        
        # For 6 players, 52 // 6 = 8. This is the key calculation to test.
        expected_start_cards = 8
        self.assertEqual(self.game.start_cards, expected_start_cards)
        self.assertEqual(self.game.current_cards, expected_start_cards)
        self.assertEqual(self.game.deal_direction, -1)
        
        self.assertIn('total_score', self.game.players[1])
        self.assertEqual(self.game.players[1]['total_score'], 0)
        print("OK")

    def test_prepare_round_and_distribution_6_players(self):
        """
        Tests card distribution for 6 players. 8 cards each, 4 left in deck.
        """
        print("\n--- Testing prepare_round and distribution (6 Players) ---")
        
        cards_to_deal = 8  # 52 // 6
        
        self.game.prepare_round(self.deck)

        # 1. Test trump suit selection
        self.assertEqual(self.game.trump_suit, 'Spades')

        # 2. Test card distribution
        for player_id in self.game.players:
            self.assertIn('cards', self.game.players[player_id])
            self.assertEqual(len(self.game.players[player_id]['cards']), cards_to_deal)
        
        # 3. Test remaining cards in the deck. 52 - (6 * 8) = 4
        self.assertEqual(len(self.deck), 4)
        print("OK")

if __name__ == '__main__':
    unittest.main()