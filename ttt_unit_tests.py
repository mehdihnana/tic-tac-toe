# ============================================================
# Tic Tac Toe Function Tests
# ------------------------------------------------------------
# Run this file to check how your functions in ttt_functions.py
# are performing. You don't need to complete all functions before
# testing — it will still run and show partial results.
#
# Run it with:
#     python ttt_unit_tests.py
# ============================================================

from ttt_functions import is_valid_move, place_move, check_winner, is_board_full

def print_result(name, passed):
    mark = "✅" if passed else "❌"
    print(f"{mark} {name}")

def test_is_valid_move():
    print("\nTesting is_valid_move...")
    board = [[" " for _ in range(3)] for _ in range(3)]
    board[1][1] = "X"

    # 1/22/26 Updated this test so that it does not crash
    # on IndexError, just reports as a failure
    tests = [
        ((0, 0), True, "empty spot valid"),
        ((1, 1), False, "occupied spot invalid"),
        ((-1, 0), False, "negative index invalid"),
        ((3, 2), False, "out of range invalid"),
        ((2, 2), True, "bottom-right empty valid"),
    ]

    for move, expected, desc in tests:
        try:
            result = is_valid_move(board, move) == expected
        except (IndexError, Exception) as e:
            # If an exception occurs, the test fails
            # You can optionally print what went wrong
            print(f"  Exception caught: {type(e).__name__}: {e}")
            result = False
        
        print_result(f"is_valid_move: {desc}", result)


def test_place_move():
    print("\nTesting place_move...")
    board = [[" " for _ in range(3)] for _ in range(3)]
    place_move(board, (0, 0), "X")
    tests = [
        (board[0][0] == "X", "places X correctly"),
    ]

    # Should not overwrite
    place_move(board, (0, 1), "O")
    tests.append((board[0][1] == "O", "places O correctly"))

    for result, desc in tests:
        print_result(f"place_move: {desc}", result)


def test_check_winner():
    print("\nTesting check_winner...")
    tests = []

    # Row win
    board = [
        ["X", "X", "X"],
        [" ", "O", " "],
        ["O", " ", " "]
    ]
    tests.append((check_winner(board) == "X", "row win detected"))

    # Column win
    board = [
        ["O", "X", " "],
        ["O", "X", " "],
        ["O", " ", "X"]
    ]
    tests.append((check_winner(board) == "O", "column win detected"))

    # Diagonal \ win
    board = [
        ["X", "O", " "],
        ["O", "X", " "],
        [" ", "O", "X"]
    ]
    tests.append((check_winner(board) == "X", r"\ diagonal win detected"))

    # Diagonal / win
    board = [
        ["X", "X", "O"],
        ["O", "O", " "],
        ["O", " ", "X"]
    ]
    tests.append((check_winner(board) == "O", "/ diagonal win detected"))

    # No winner
    board = [
        ["X", "O", "X"],
        ["O", "O", "X"],
        ["X", "X", "O"]
    ]
    tests.append((check_winner(board) is None, "no winner when full board"))

    # Empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    tests.append((check_winner(board) is None, "no winner on empty board"))

    for result, desc in tests:
        print_result(f"check_winner: {desc}", result)


def test_is_board_full():
    print("\nTesting is_board_full...")
    tests = []

    # Empty
    board = [[" " for _ in range(3)] for _ in range(3)]
    tests.append((is_board_full(board) == False, "empty board not full"))

    # Partially filled
    board[0][0] = "X"
    tests.append((is_board_full(board) == False, "partially filled board not full"))

    # Full
    board = [
        ["X", "O", "X"],
        ["O", "O", "X"],
        ["X", "X", "O"]
    ]
    tests.append((is_board_full(board) == True, "fully filled board detected as full"))

    for result, desc in tests:
        print_result(f"is_board_full: {desc}", result)


if __name__ == "__main__":
    print("Running Tic Tac Toe function tests...")
    test_is_valid_move()
    test_place_move()
    test_check_winner()
    test_is_board_full()
    print("\nTesting complete.\n")
