def is_valid_move(board, move):
    """
    Checks if a move is valid.
    move is a tuple (row, col).
    Returns True if the spot is empty and within the board bounds, otherwise False.
    """
    row, col = move

    if row < 0 or row > 2 or col < 0 or col > 2:
        return False

    return board[row][col] == " "


def place_move(board, move, player):
    """
    Places the player's mark ('X' or 'O') on the board.
    """
    row, col = move
    board[row][col] = player
    return board


def check_winner(board):
    """
    Checks if there is a winner.
    Returns 'X', 'O', or None.
    """

    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonal \
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    # Check diagonal /
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def is_board_full(board):
    """
    Returns True if there are no empty spaces left.
    """
    for row in board:
        for cell in row:
            if cell == " ":
                return False

    return True