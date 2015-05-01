from board import *

def sudokuSolve(board):
    """The solver function which will be called with all the different types of value selection and tile selection."""
    #board.p()
    print board.squaresFilled
    bsize = board.boardSize
    tileList = chooseUnassignedTiles(board, "MCV")

    # for i in range(bsize):
    #     for j in range(bsize):
    #         tile = board.board[i][j]
            # if tile.cellVal == 0:
    for tile in tileList:
        valList = chooseValue(board, tile, "LCV")
        for value in valList:
            newBoard = copy.deepcopy(board)
            result = False
            # True unless no possible vals in any modified square
            if newBoard.addValue(value, tile.row, tile.column, True):
                if newBoard.isFull():
                    return newBoard
                result = sudokuSolve(newBoard)
                if result is not False:
                    return result
    return False

def chooseUnassignedTiles(board, typ):
    """Returns a tile to assign to. Implementing Backtracking"""
    tileList = []
    bsize = board.boardSize
    for i in range(bsize):
            for j in range(bsize):
                tile = board.board[i][j]
                if tile.cellVal == 0:
                    tileList.append(tile)
    if typ == "BASIC":
        return tileList

    if typ == "MCV":
        return sorted(tileList, key = lambda tile: -checkAffectedTiles(board, tile))

    if typ == "MRV":
        return sorted(tileList, key = lambda tile: len(tile.possibleVals))

def checkAffectedTiles(board, tile):
    affectedTiles = 0
    column = tile.column
    row = tile.row
    section = tile.boardSection
    for i in range(board.boardSize):
        for j in range(board.boardSize):
            cell = board.board[i][j]
            if cell.boardSection == section and cell.cellVal == 0:
                affectedTiles += 1
                continue
            if board.board[i][column].cellVal == 0 and i != row:
                affectedTiles += 1
            if board.board[row][i].cellVal == 0 and i != column:
                affectedTiles += 1
    return affectedTiles


def chooseValue(board, tile, typ):
    """Given a tile, chooses a value to assign"""
    if typ == "BASIC":
        return list(tile.possibleVals)
    if typ == "LCV":
        l = list(tile.possibleVals)
        return sorted(l, key = lambda v: board.removeValCount(tile, v))



def countRemovedPossibilities(board, tile, val):
    for i in range(board.boardSize):
        for j in range(board.boardSize):
            cell = board.board[i][j]
            if cell.boardSection == tile.boardSection and cell.cellVal == 0:
                valConstraints += boardremoveValCount(val)
                continue
            if board.board[i][column].cellVal == 0 and i != row:
                valConstraints += 1
            if board.board[row][i].cellVal == 0 and i != column:
                valConstraints += 1
        #

