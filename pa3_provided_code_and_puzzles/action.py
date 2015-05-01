from board import *

def sudokuSolve(board):
    """The solver function which will be called with all the different types of value selection and tile selection."""
    #board.p()
    #print board.firstBlankRow, board.firstBlankColumn
    print board.squaresFilled
    bsize = board.boardSize
    chosenTile = chooseUnassignedTile(board, "BASIC")

    valList = chooseValue(board, chosenTile, "BASIC")
    for value in valList:
        newBoard = copy.deepcopy(board)
        result = False
        # True unless no possible vals in any modified square
        if newBoard.addValue(value, chosenTile.row, chosenTile.column, True):
            if newBoard.isFull():
                return newBoard
            result = sudokuSolve(newBoard)
            if result is not False:
                return result
    return False

def chooseUnassignedTile(board, typ):
    """Returns a tile to assign to. Implementing Backtracking"""
    if typ == "BASIC":
        return board.board[board.firstBlankRow][board.firstBlankColumn]

    if typ == "MCV":
        if len(board.minRemainingValues) == 0:
            board.findMinimumRemainingValues()
        return board.minRemainingValues[0]

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

