from board import *

def backTracking(board):
    """Simplest Backtracking Function, it starts at the top left of the board and then just runs through all possible values."""
    bsize = board.boardSize
    for i in range(bsize):
        for j in range(bsize):
            tile = board.board[i][j]
            if tile.cellVal == 0:
                for value in tile.possibleVals:
                    tempBoard = copy.deepcopy(board)
                    tempBoard.addValue(value, i, j)
                    tempBoard.p()
                    if i == bsize - 1 & j == bsize - 1:
                        if tempBoard.checkComplete():
                            return tempBoard
                    if tempBoard.checkConsistent():
                        result = backTracking(tempBoard)
                    if result != False:
                        return result
    return False
