import unittest
from unittest.mock import patch
from game import Game
from kachuful import kachuFul
from deck import CardDeck
from players import Player

class TestKachufulLogic(unittest.TestCase):

    def setUp(self):
        """Set up a standard game with 4 players for logic testing."""
        players = [Player(i, f"Player {i}") for i in range(1, 5)]
        player_dict = {p.player_id: {'player_name': p.player_name} for p in players}

        kachuful_game_setup = Game(
            game_id=1,
            game_name="Kachuful-4p",
            no_of_cards=0,
            players=player_dict
        )
        self.game = kachuFul(kachuful_game_setup, no_of_players=4)
        self.deck = CardDeck().create_deck()

    def test_initialization_4_players(self):
        """Tests that __init__ calculates the correct starting card count for 4 players."""
        print("\n--- Testing __init__ (4 Players) ---")
        self.assertEqual(self.game.no_of_players, 4)
        # For 4 players, 52 // 4 = 13
        self.assertEqual(self.game.start_cards, 13)
        self.assertEqual(self.game.current_cards, 13)
        self.assertEqual(self.game.deal_direction, -1)
        self.assertEqual(self.game.dealer_index, 0)
        print("OK")

    def test_end_round_card_and_dealer_progression(self):
        """Tests that card counts and dealer index update correctly across rounds."""
        print("\n--- Testing end_round progression ---")
        # Initial state: 13 cards, dealer is Player 1 (index 0)
        self.assertEqual(self.game.current_cards, 13)
        self.assertEqual(self.game.dealer_index, 0)

        # After round 1
        self.game.end_round()
        self.assertEqual(self.game.current_cards, 12, "Should have 12 cards")
        self.assertEqual(self.game.dealer_index, 1, "Dealer should be Player 2")

        # Speed through to 1 card
        for _ in range(10):
            self.game.end_round()
        
        self.assertEqual(self.game.current_cards, 2, "Should have 2 cards")
        self.game.end_round()
        self.assertEqual(self.game.current_cards, 1, "Should have 1 card")
        
        # Test direction flip
        self.game.end_round()
        self.assertEqual(self.game.deal_direction, 1, "Direction should flip to increasing")
        self.assertEqual(self.game.current_cards, 2, "Should now have 2 cards")

        # Test cycle reset
        # Go from 2 up to 13 (11 more rounds)
        for _ in range(11):
            self.game.end_round()
        
        self.assertEqual(self.game.current_cards, 13, "Should be back at 13 cards")
        
        # Next round should reset the cycle
        self.game.end_round()
        self.assertEqual(self.game.current_cards, 13, "Should reset to 13 cards")
        self.assertEqual(self.game.deal_direction, -1, "Direction should reset to decreasing")
        print("OK")

    @patch('builtins.input', side_effect=['5', '3', '1', '2'])
    def test_get_player_calls_valid(self, mock_input):
        """Tests a round of valid calls."""
        print("\n--- Testing valid player calls ---")
        self.game.current_cards = 10 # Set a specific number for predictability
        self.game.dealer_index = 0 # Player 1 is the dealer
        
        # Call order should be 2, 3, 4, 1(dealer)
        self.game.calls()

        self.assertEqual(self.game.players[2]['no_of_hands'], 5)
        self.assertEqual(self.game.players[3]['no_of_hands'], 3)
        self.assertEqual(self.game.players[4]['no_of_hands'], 1)
        self.assertEqual(self.game.players[1]['no_of_hands'], 2)
        print("OK")

    @patch('builtins.input', side_effect=['11', '5', '3', '1', '2'])
    def test_get_player_calls_invalid_range(self, mock_input):
        """Tests that calls outside the allowed range are rejected."""
        print("\n--- Testing invalid range call ---")
        self.game.current_cards = 10
        self.game.dealer_index = 0

        # Player 2 first tries 11 (invalid), then 5 (valid)
        self.game.calls()
        
        self.assertEqual(self.game.players[2]['no_of_hands'], 5)
        self.assertEqual(mock_input.call_count, 5) # 1 invalid + 4 valid calls
        print("OK")

    @patch('builtins.input', side_effect=['4', '3', '1', '2', '0'])
    def test_get_player_calls_dealer_restriction(self, mock_input):
        """Tests that the dealer is prevented from making the forbidden call."""
        print("\n--- Testing dealer's forbidden call ---")
        self.game.current_cards = 10
        self.game.dealer_index = 0 # Player 1 is the dealer

        # Call order: 2, 3, 4, 1(dealer)
        # Calls from 2, 3, 4 are 4, 3, 1. Total = 8.
        # Forbidden call for dealer (Player 1) is 10 - 8 = 2.
        # The mock input has the dealer try '2' first, then '0'.
        self.game.calls()

        self.assertEqual(self.game.players[1]['no_of_hands'], 0)
        self.assertEqual(mock_input.call_count, 5) # 3 non-dealers + 1 invalid dealer + 1 valid dealer
        print("OK")


class TestKachuful6Players(unittest.TestCase):

    def setUp(self):
        """
        This method now sets up a game with 6 players to test the division logic.
        """
        # 1. Setup 6 players
        players = [Player(i, f"Player {i}") for i in range(1, 7)]
        player_dict = {p.player_id: {'player_name': p.player_name} for p in players}

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
