from teen_patti import TeenPatti, heirarchy
from game import Game

# We need a game instance to create a TeenPatti instance.
# The arguments don't matter for this specific test.
g_test = Game(1, "Test", 3) 
tp_test = TeenPatti(g_test, 3)

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

# --- Test Case 2: A hand that is NOT a Trio ---
print("--- Testing for a Non-Trio ---")
non_trio_hand = [('Ace', 'Spades'), ('King', 'Hearts'), ('Ace', 'Clubs')]
result_rank_2, _ = tp_test.evaluate_hands(non_trio_hand)

print(f"Hand: {non_trio_hand}")
print(f"Detected Rank Value: {result_rank_2}")
print(f"Expected Rank Value: None")

if result_rank_2 is None:
    print("PASS: Correctly returned None for a non-Trio hand.")
else:
    print("FAIL: Incorrectly identified a rank.")

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
