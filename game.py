# game.py
import random
from ttt_functions import is_valid_move, place_move, check_winner, is_board_full

def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("\n   1   2   3")
    for i, row in enumerate(board):
        label = chr(ord("A") + i)
        print(f"{label}  " + " | ".join(row))
        if i < 2:
            print("  ---+---+---")
    print()

def parse_move(move_str):
    """Convert A1, B2, etc. into (row, col) tuples (0–2)."""
    if len(move_str) != 2:
        return None
    row_char, col_char = move_str[0].upper(), move_str[1]
    if row_char not in "ABC" or col_char not in "123":
        return None
    row = ord(row_char) - ord("A")
    col = int(col_char) - 1
    return (row, col)

def main():
    print("Welcome to Tic Tac Toe!")
    print("Enter your moves like A1, B2, etc.\n")

    # Ask if they want to play against another player or a bot
    mode = ""
    while mode not in ["1", "2"]:
        mode = input("Enter 1 for 2-Player mode, or 2 to play against the bot: ").strip()

    use_bot = (mode == "2")
    if use_bot:
        from bot import get_bot_move
        print("You are Player X. The bot will play as O.")
    else:
        print("2-Player mode selected!")

    board = create_board()
    current_player = "X"

    print_board(board)

    while True:
        # Bot or human turn
        if use_bot and current_player == "O":
            move = get_bot_move(board, "O", "X")
            print(f"Bot chooses {chr(ord('A') + move[0])}{move[1] + 1}")
        else:
            move_str = input(f"Player {current_player}, enter your move: ").strip()
            move = parse_move(move_str)
            if not move:
                print("Invalid format! Use A1, B2, etc.")
                continue

        # Validate
        if not is_valid_move(board, move):
            print("That move is not valid. Try again.")
            continue

        # Place move
        place_move(board, move, current_player)
        print_board(board)

        # Check for win
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break

        # Check for tie
        if is_board_full(board):
            print("It's a tie!")
            break

        # Switch turn
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
