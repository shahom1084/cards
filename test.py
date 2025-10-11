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
    print("✅ PASSED: Correctly identified a Trio.")
else:
    print("❌ FAILED: Did not identify a Trio.")

print("-" * 20)

# --- Test Case 2: A hand that is NOT a Trio ---
print("--- Testing for a Non-Trio ---")
non_trio_hand = [('Ace', 'Spades'), ('King', 'Hearts'), ('Ace', 'Clubs')]
result_rank_2, _ = tp_test.evaluate_hands(non_trio_hand)

print(f"Hand: {non_trio_hand}")
print(f"Detected Rank Value: {result_rank_2}")
print(f"Expected Rank Value: None")

if result_rank_2 is None:
    print("✅ PASSED: Correctly returned None for a non-Trio hand.")
else:
    print("❌ FAILED: Incorrectly identified a rank.")

print("-" * 20)
