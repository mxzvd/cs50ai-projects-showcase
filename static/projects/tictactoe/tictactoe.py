"""
Tic Tac Toe Player
"""

import math, sys, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    moves = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] in ("X", "O"):
                moves += 1
    
    return "X" if moves % 2 == 0 else "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    options = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                options.add((i, j))
    
    return options


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid move")
    
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    scores = {
        "X": [0] * 8,
        "O": [0] * 8
    }
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                continue
            scores[board[i][j]][i] += 1
            scores[board[i][j]][j + 3] += 1
            if i == j:
                scores[board[i][j]][6] += 1
            if i == 2 - j:
                scores[board[i][j]][7] += 1
    
    for i in range(8):
        if scores["X"][i] == 3:
            return X
        if scores["O"][i] == 3:
            return O
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result == None:
        return 0
    elif result == "X":
        return 1
    else:
        return -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    action_to_return = None
    if player(board) == "X":
        v = -sys.maxsize
        for action in actions(board):
            action_value = max_value(result(board, action))
            if action_value >= v:
                action_to_return = action
                v = action_value
    else:
        v = sys.maxsize
        for action in actions(board):
            action_value = min_value(result(board, action))
            if action_value <= v:
                action_to_return = action
                v = action_value
    
    return action_to_return

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -1000
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = 1000
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
