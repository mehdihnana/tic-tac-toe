# bot.py
import random

def get_bot_move(board, bot_symbol, player_symbol):
    """
    Simple rule-based bot:
      1) Win if possible (two bot symbols + empty)
      2) Block opponent win (two opponent symbols + empty)
      3) Build toward a win (one bot symbol + two empties)
      4) Otherwise pick a random empty cell
    Always returns a valid (row, col) tuple or raises if the board is full.
    """

    def find_line(symbol, needed_self, needed_empty):
        # check rows and columns
        for i in range(3):
            row = board[i]
            if row.count(symbol) == needed_self and row.count(" ") == needed_empty:
                for j in range(3):
                    if row[j] == " ":
                        return (i, j)
            col = [board[r][i] for r in range(3)]
            if col.count(symbol) == needed_self and col.count(" ") == needed_empty:
                for r in range(3):
                    if board[r][i] == " ":
                        return (r, i)
        return None

    def find_diag(symbol, needed_self, needed_empty):
        diags = [
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]
        for diag in diags:
            symbols = [board[r][c] for r, c in diag]
            if symbols.count(symbol) == needed_self and symbols.count(" ") == needed_empty:
                for r, c in diag:
                    if board[r][c] == " ":
                        return (r, c)
        return None

    # 1) Try to win
    move = find_line(bot_symbol, 2, 1) or find_diag(bot_symbol, 2, 1)
    if move:
        return move

    # 2) Try to block
    move = find_line(player_symbol, 2, 1) or find_diag(player_symbol, 2, 1)
    if move:
        return move

    # 3) Try building toward a win
    move = find_line(bot_symbol, 1, 2) or find_diag(bot_symbol, 1, 2)
    if move:
        return move

    # 4) Random fallback from remaining empty cells
    possible_moves = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    if possible_moves:
        return random.choice(possible_moves)

    # No moves available (shouldn't be reached if game loop checks for full board)
    raise RuntimeError("No valid moves available: board appears full.")
