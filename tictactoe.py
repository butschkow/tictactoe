import copy

"""
Tic Tac Toe Player (DONE!)
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    # return [[O, EMPTY, X], [EMPTY, X, O], [EMPTY, EMPTY, EMPTY]]


def player(board):
    if terminal(board):
        return None
   
    Xs = 0
    Os = 0
    for row in board:
        for line in row:
            if line == X: 
                Xs += 1
            elif line == O:
                Os += 1
    if Os >= Xs:
        return X
    else:
        return O


def actions(board):

    available = set()
    rowCount = -1
    
    for row in board:
        rowCount = rowCount + 1
        lineCount = -1
        for line in row:
            lineCount = lineCount + 1
            if(line == None):
                av = tuple([rowCount, lineCount])
                available.add(av)
                # print(av)
    return available


def result(board, move): # move (i,j)
    returnBoard = []
    currentPlayer = player(board)
    returnBoard = copy.deepcopy(board)

    # check for possible illegal move
    if returnBoard[move[0]][move[1]] != EMPTY:
         raise Exception("Illegal move passed, cannot continue!")
    returnBoard[move[0]][move[1]] = currentPlayer
    return returnBoard
    # Returns the board that results from making move (i, j) on the board.

def winner(board):
    if(utility(board) == 1):
        return X
    if(utility(board) == -1):
        return O
    if(utility(board) == 0):
        return EMPTY
    # Returns the winner of the game, if there is one.


def terminal(board):
    # print(actions(board))
    if len(actions(board)) == 0 or utility(board) != 0:
        return True
    else:
        return False


def utility(board):
    if (board[0][0] == X and board[1][0] == X and board[2][0] == X): # hori top 
        return 1
    if (board[0][0] == X and board[0][1] == X and board[0][2] == X): # vert top left
        return 1
    if (board[0][0] == X and board[1][1] == X and board[2][2] == X): # diagonal 1
        return 1
    if (board[0][2] == X and board[1][1] == X and board[2][0] == X): # diagonal 2
        return 1
    if (board[1][0] == X and board[1][1] == X and board[1][2] == X): # middle hori
        return 1
    if (board[0][1] == X and board[1][1] == X and board[2][1] == X): # middle vert
        return 1
    if (board[2][0] == X and board[2][1] == X and board[2][2] == X): # bottom hori
        return 1
    if (board[0][2] == X and board[1][2] == X and board[2][2] == X): # vert top right
        return 1

    if (board[0][0] == O and board[1][0] == O and board[2][0] == O): # hori top 
        return -1
    if (board[0][0] == O and board[0][1] == O and board[0][2] == O): # vert top left
        return -1
    if (board[0][0] == O and board[1][1] == O and board[2][2] == O): # diagonal 1
        return -1
    if (board[0][2] == O and board[1][1] == O and board[2][0] == O): # diagonal 2
        return -1
    if (board[1][0] == O and board[1][1] == O and board[1][2] == O): # middle hori
        return -1
    if (board[0][1] == O and board[1][1] == O and board[2][1] == O): # middle vert
        return -1
    if (board[2][0] == O and board[2][1] == O and board[2][2] == O): # bottom hori
        return -1
    if (board[0][2] == O and board[1][2] == O and board[2][2] == O): # vert top right
        return -1
    return 0

def minimax(board):
  
    solution = []

    if terminal(board):
        return None
    # Keep looping until solution found
    while True:
        testBoard = set()
        testBoard = copy.deepcopy(board)
        currentPlayer = player(board)

        for action in actions(testBoard):
            testResult = result(testBoard, action)
            
            # check for immediate win
            if(terminal(testResult)):
                return action
                          
            total = calculatePath(testResult, action)
            solution.append([action, total])
            print(solution)

        print("Player: ", currentPlayer)
        if currentPlayer == O:
            record_with_lowest_value = min(solution, key=lambda x: x[1])
        else:
            record_with_lowest_value = max(solution, key=lambda x: x[1])
        return record_with_lowest_value[0]


def calculatePath(board, action):
    pathCost = 0
    currentPlayer = player(board)
    testBoard = set()
    testBoard = copy.deepcopy(board)
        
    for action in actions(testBoard):
        testResult = result(testBoard, action)
        if(terminal(testResult)):
            if currentPlayer == X and utility(testResult) == 1:
                pathCost = pathCost + 1
            else:
                pathCost = pathCost - 1
            return pathCost        
        else:
            pathCost = pathCost + calculatePath(testResult, action) 
    return pathCost