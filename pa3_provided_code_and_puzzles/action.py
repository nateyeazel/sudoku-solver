from board import *

def backTracking(board):
    """Simplest Backtracking Function, it starts at the top left of the board and then just runs through all possible values."""
    bsize = board.boardSize
    for i in range(bsize):
        for j in range(bsize):
            tile = board[i][j]
            if tile.cellVal == 0:
                for value in tile.possibleVals:
                    tempBoard = copy.deepcopy(board)
                    tempBoard.addValue(value, i, j)
                    if i == bsize - 1 & j == bsize - 1:
                        if tempBoard.checkComplete():
                            return tempBoard
                    if tempBoard.checkConsistent():
                        result = backTracking(tempBoard)
                    if result != False:
                        return result
            return False




def boardTest(file):
    sb = parse_file(file)
    m = MyBoard(sb, len(sb))
    m.p()

def test():
    sb = parse_file("input_puzzles/easy/4_4.sudoku")
    m = MyBoard(sb, len(sb))
    m.addValue(3, 0, 3)
    m.addValue(1, 0, 2)
    m.p()
    return m.checkConsistent()
