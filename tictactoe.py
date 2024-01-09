"""
Tic Tac Toe Player
"""
import copy
import math

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
    flat_board = [i for j in board for i in j]
    if flat_board.count(EMPTY) == 0:
        return None
    if flat_board.count(EMPTY) % 2 == 0:
        return O
    return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return [(x, y) for x, i in enumerate(board) for y, j in enumerate(i) if j == EMPTY]


def result(board, action):
    if board[action[0]][action[1]] != EMPTY:
        raise Exception
    board = copy.deepcopy(board)

    board[action[0]][action[1]] = player(board)
    return board


def winner(board):
    board = [j for i in board for j in i]
    if any(O == board[a] == board[b] == board[c] for a,b,c in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]):
        return O
    if any(X == board[a] == board[b] == board[c] for a,b,c in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]):
        return X
    return None


def terminal(board):
    return all([True if j != EMPTY else False for i in board for j in i]) or bool(winner(board))


def utility(board):
    map = {
        X: 1,
        O: -1,
        None: 0
    }
    return map[winner(board)]


def minimax(board):
    map = {O: -1, X: 1}

    def maximize(board):
        if terminal(board):
            return utility(board)
        best_score = -100000
        for i in actions(board):
            score = maximize(result(board, i)) * map[player(board)]
            if score > best_score:
                best_score = score
        return best_score

    best_score = [-100000, None]
    for i in actions(board):
        score = maximize(result(board, i)) * -1
        print(score, i, board, player(board))
        if score > best_score[0]:
            best_score[0] = score
            best_score[1] = i

    return best_score[1]





