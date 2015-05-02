from board import *

def sudokuSolve(board, fwd, mrv, mcv, lcv):
    """The solver function which will be called with all the different types of value selection and tile selection."""
    #board.p()
    #print board.firstBlankRow, board.firstBlankColumn
    cellHeuristic = "BASIC"
    valueHeuristic = "BASIC"
    if mrv:
        cellHeuristic = "MRV"
    if mcv:
        cellHeuristic = "MCV"
    if lcv:
        valueHeuristic = "LCV"

    print board.squaresFilled
    bsize = board.boardSize
    chosenCell = chooseUnassignedCell(board, cellHeuristic)

    valList = chooseValue(board, chosenCell, valueHeuristic)
    for value in valList:
        newBoard = copy.deepcopy(board)
        result = False
        # True unless no possible vals in any modified square
        if newBoard.addValue(value, chosenCell.row, chosenCell.column, fwd):
            if newBoard.isFull():
                return newBoard
            result = sudokuSolve(newBoard, fwd, mrv, mcv, lcv)
            if result is not False:
                return result
    return False

def chooseUnassignedCell(board, typ):
    """Returns a cell to assign to. Implementing Backtracking"""
    if typ == "BASIC":
        return board.blankCells[0]

    if typ == "MRV":
        return sorted(board.blankCells, key=lambda cell: len(cell.possibleVals))[0]

    if typ == "MCV":
        return sorted(board.blankCells, key=lambda cell: cell.constrainedCells)[0]

def checkAffectedCells(board, cell):
    affectedcells = 0
    column = cell.column
    row = cell.row
    section = cell.boardSection
    for i in range(board.boardSize):
        for j in range(board.boardSize):
            cell = board.board[i][j]
            if cell.boardSection == section and cell.cellVal == 0:
                affectedcells += 1
                continue
            if board.board[i][column].cellVal == 0 and i != row:
                affectedcells += 1
            if board.board[row][i].cellVal == 0 and i != column:
                affectedcells += 1
    return affectedcells


def chooseValue(board, cell, typ):
    """Given a cell, chooses a value to assign"""
    if typ == "BASIC":
        return list(cell.possibleVals)
    if typ == "LCV":
        l = list(cell.possibleVals)
        return sorted(l, key = lambda v: board.removeValCount(cell, v))

