"""
Tic Tac Toe Player
"""

import copy

N = 3
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
    count_of_O = 0
    count_of_X = 0
    for row in board:
        for element in row:
            if element == X:
                count_of_X += 1
            elif element == O:
                count_of_O += 1
    if count_of_X == count_of_O + 1:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ret = set()
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            if element == EMPTY:
                ret.add((i, j))
    return ret


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_element = player(board)
    i, j = action
    if board[i][j] != EMPTY:
        raise ValueError("Selected action is not primited")
    if not (0 <= i < N and 0 <= j < N):
        raise ValueError("Selected action parts should not be negetive nor greater than 2")
    ret_board = copy.deepcopy(board)
    ret_board[i][j] = player_element
    return ret_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == EMPTY:
            continue
        is_equal = True
        for j in range(3):
            if board[i][0] != board[i][j]:
                is_equal = False
        if is_equal:
            return board[i][0]

    for j in range(3):
        if board[0][j] == EMPTY:
            continue
        is_equal = True
        for i in range(3):
            if board[0][j] != board[i][j]:
                is_equal = False
        if is_equal:
            return board[0][j]

    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    # Check if the board is full
    for row in board:
        for element in row:
            if element == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def max_value(board):
    if player(board) != X:
        raise ValueError("Player should be X in max_value")
    if terminal(board):
        return (utility(board), None)
    available_actions = actions(board)
    best_action = None
    best_action_val = -2
    for action in available_actions:
        new_board = result(board, action)
        action_val, opponent_action = min_value(new_board)
        if action_val > best_action_val:
            best_action = action
            best_action_val = action_val
    return best_action_val, best_action


def min_value(board):
    if player(board) != O:
        raise ValueError("Player should be O in min_value")
    if terminal(board):
        return (utility(board), None)
    available_actions = actions(board)
    best_action = None
    best_action_val = 2
    for action in available_actions:
        new_board = result(board, action)
        action_val, opponent_action = max_value(new_board)
        if action_val < best_action_val:
            best_action_val = action_val
            best_action = action
    return best_action_val, best_action


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        val, action = max_value(board)
    else:
        val, action = min_value(board)
    return action
