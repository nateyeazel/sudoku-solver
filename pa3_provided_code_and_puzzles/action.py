from board import *

def sudokuSolve(board, fwd, mrv, mcv, lcv):
    """The solver function which will be called with all the different types of value selection and tile selection."""
    cellHeuristic = "BASIC"
    valueHeuristic = "BASIC"
    if mrv:
        cellHeuristic = "MRV"
    if mcv:
        cellHeuristic = "MCV"
    if lcv:
        valueHeuristic = "LCV"

    # print board.squaresFilled
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


def chooseValue(board, cell, typ):
    """Given a cell, chooses a value to assign"""
    if typ == "BASIC":
        return list(cell.possibleVals)
    if typ == "LCV":
        return sorted(cell.possibleVals, key = lambda value: board.removedValCount(cell, value))

