from board import *

def sudokuSolve(board):
    """Simplest Backtracking Function, it starts at the top left of the board and then just runs through all possible values."""
    bsize = board.boardSize
    tileList = chooseUnassignedTiles(board, "BASIC")

    # for i in range(bsize):
    #     for j in range(bsize):
    #         tile = board.board[i][j]
            # if tile.cellVal == 0:
    for tile in tileList:
        valList = chooseValue(board, tile, "BASIC")

        for value in valList.copy():
            newBoard = copy.deepcopy(board)
            newBoard.addValue(value, tile.row, tile.column, True)
            #newBoard.p()
            result = False
            if newBoard.checkConsistent(tile, "FWD"):
                if newBoard.isFull():
                    return newBoard
                result = sudokuSolve(newBoard)
                if result != False:
                    return result
    return False

def chooseUnassignedTiles(board, typ):
    """Returns a tile to assign to. Implementing Backtracking"""
    tileList = []
    bsize = board.boardSize
    if typ == "BASIC":
        for i in range(bsize):
            for j in range(bsize):
                tile = board.board[i][j]
                if tile.cellVal == 0:
                    tileList.append(tile)
        return tileList

    # if typ == "MCV":
    #     #do later

    # if typ == "MRV":
        #DO LATER



def chooseValue(board, tile, typ):
    """Given a tile, chooses a value to assign"""
    if typ == "BASIC":
        return tile.possibleVals
    # if typ == "LCV"
    #     #

