from teen_patti import TeenPatti, heirarchy, TeenPattiMoves
from game import Game

# We need a game instance to create a TeenPatti instance.
# The arguments don't matter for this specific test.
g_test = Game(1, "Test", 3)
# Add players to the game instance
for i in range(1, 4):
    g_test.add_player(i)

tp_test = TeenPatti(g_test, 3,10)

# --- Test Case 1: A hand that IS a Trio ---
print("--- Testing for a Trio ---")
trio_hand = [('Ace', 'Spades'), ('Ace', 'Hearts'), ('Ace', 'Clubs')]
result_rank, result_cards = tp_test.evaluate_hands(trio_hand)

print(f"Hand: {trio_hand}")
print(f"Detected Rank Value: {result_rank}")
print(f"Expected Rank Value: {heirarchy.TRIO.value}")

if result_rank == heirarchy.TRIO.value:
    print("PASS: Correctly identified a Trio.")
else:
    print("FAIL: Did not identify a Trio.")

print("-" * 20)



print("-" * 20)

# --- Test Case 3: A hand that IS a Straight (Unpure Sequence) ---
print("--- Testing for a Straight (Unpure Sequence) ---")
straight_hand = [('8', 'Spades'), ('9', 'Hearts'), ('10', 'Clubs')]
result_rank_3, _ = tp_test.evaluate_hands(straight_hand)

print(f"Hand: {straight_hand}")
print(f"Detected Rank Value: {result_rank_3}")
print(f"Expected Rank Value: {heirarchy.STRAIGHT.value}")

if result_rank_3 == heirarchy.STRAIGHT.value:
    print("PASS: Correctly identified a Straight.")
else:
    print("FAIL: Did not identify a Straight.")

print("-" * 20)

# --- Test Case 5: A hand that IS a Flush (color) ---
print("--- Testing for a  Flush (color) ---")
flush_hand = [('4', 'Hearts'), ('6', 'Hearts'), ('9', 'Hearts')]
result_rank_3, _ = tp_test.evaluate_hands(flush_hand)

print(f"Hand: {flush_hand}")
print(f"Detected Rank Value: {result_rank_3}")
print(f"Expected Rank Value: {heirarchy.FLUSH.value}")

if result_rank_3 == heirarchy.FLUSH.value:
    print("PASS: Correctly identified a Flush.")
else:
    print("FAIL: Did not identify Straight Flush.")

print("-" * 20)
# --- Test Case 6: A hand that IS a pair ---
print("--- Testing for a  pair ---")
pair_hand = [('4', 'Hearts'), ('4', 'Spades'), ('9', 'Hearts')]
result_rank_2, _ = tp_test.evaluate_hands(pair_hand)

print(f"Hand: {pair_hand}")
print(f"Detected Rank Value: {result_rank_2}")
print(f"Expected Rank Value: {heirarchy.PAIR.value}")

if result_rank_2 == heirarchy.PAIR.value:
    print("PASS: Correctly identified a PAIR.")
else:
    print("FAIL: Did not identify a pair.")

print("-" * 20)


# --- TDD Test for rules() method: No Ties ---
print("--- TDD for rules(): No-tie scenario ---")
# Player 2 has the best hand (Flush)
players_no_tie = {
    1: {'cards': [('Ace', 'H'), ('Ace', 'S'), ('2', 'C')]},
    2: {'cards': [('5', 'D'), ('8', 'D'), ('King', 'D')]},
    3: {'cards': [('7', 'H'), ('9', 'S'), ('Jack', 'C')]}
}

winner = tp_test.rules(players_no_tie)
print(f"Winner: {winner}, Expected: 2")
if winner == 2:
    print("PASS: Correctly identified the winner in a no-tie scenario.")
else:
    print("FAIL: Did not identify the correct winner.")

print("-" * 20)

# --- TDD Test for rules() method: Tie Scenario ---
print("--- TDD for rules(): Tie scenario ---")
# Player 1 and 2 have a pair, but Player 1 has a higher pair.
players_tie = {
    1: {'cards': [('Ace', 'H'), ('Ace', 'S'), ('2', 'C')]},
    2: {'cards': [('King', 'D'), ('King', 'H'), ('3', 'S')]},
    3: {'cards': [('7', 'H'), ('9', 'S'), ('9', 'C')]}
}

winner_tie = tp_test.rules(players_tie)
print(f"Winner: {winner_tie}, Expected: 1")
if winner_tie == 1:
    print("PASS: Correctly identified the winner in a tie-scenario.")
else:
    print("FAIL: Did not identify the correct winner in a tie-scenario.")

print("-" * 20)

# --- Tests for TeenPattiMoves ---
print("--- Testing TeenPattiMoves ---")
moves_test_game = Game(2, "Moves Test", 3)
for i in range(1, 4):
    moves_test_game.add_player(i)

moves_test = TeenPattiMoves(moves_test_game, 3, 100)
moves_test.players[1]['money'] = 1000
moves_test.players[2]['money'] = 1000
moves_test.players[3]['money'] = 1000


# Test for raise_pot
print("--- Testing raise_pot ---")
moves_test.raise_pot(50)
print(f"Pot value: {moves_test.pot_value}, Expected: 150")
if moves_test.pot_value == 150:
    print("PASS: Correctly raised the pot value.")
else:
    print("FAIL: Did not raise the pot value correctly.")
print("-" * 20)

# Test for pack
print("--- Testing pack ---")
moves_test.pack(1)
print(f"Player 1 has packed: {moves_test.players[1]['has_packed']}, Expected: True")
if moves_test.players[1]['has_packed']:
    print("PASS: Correctly packed the player.")
else:
    print("FAIL: Did not pack the player.")
print("-" * 20)

# Test for chaal (seen player)
print("--- Testing chaal (seen player) ---")
moves_test.players[2]['is_seen'] = True
initial_money = moves_test.players[2]['money']
moves_test.chaal(2, 200)
print(f"Player 2 money: {moves_test.players[2]['money']}, Expected: {initial_money - 200}")
if moves_test.players[2]['money'] == initial_money - 200:
    print("PASS: Correctly deducted bet amount for seen chaal.")
else:
    print("FAIL: Incorrect deduction for seen chaal.")
print("-" * 20)

# Test for chaal (unseen player)
print("--- Testing chaal (unseen player) ---")
result = moves_test.chaal(3, 200)
print(f"Result: {result}, Expected: You can't play chaal without seeing your cards.")
if result == "You can't play chaal without seeing your cards.":
    print("PASS: Correctly handled chaal for unseen player.")
else:
    print("FAIL: Incorrectly handled chaal for unseen player.")
print("-" * 20)

# Test for blind (unseen player)
print("--- Testing blind (unseen player) ---")
initial_money = moves_test.players[3]['money']
moves_test.blind(3, 100)
print(f"Player 3 money: {moves_test.players[3]['money']}, Expected: {initial_money - 100}")
if moves_test.players[3]['money'] == initial_money - 100:
    print("PASS: Correctly deducted bet amount for blind.")
else:
    print("FAIL: Incorrect deduction for blind.")
print("-" * 20)

# Test for blind (seen player)
print("--- Testing blind (seen player) ---")
result = moves_test.blind(2, 100)
print(f"Result: {result}, Expected: you can't play blind")
if result == "you can't play blind":
    print("PASS: Correctly handled blind for seen player.")
else:
    print("FAIL: Incorrectly handled blind for seen player.")
print("-" * 20)