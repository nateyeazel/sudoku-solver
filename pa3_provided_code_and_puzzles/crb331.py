#!/usr/bin/env python

# crb331 - Collin Barnwell and npy259 - Nathan Yeazel

import struct, string, math, copy

globalcount = 0


class SudokuBoard:
    """This will be the sudoku board game object your player will manipulate."""

    def __init__(self, size, board):
      """the constructor for the SudokuBoard"""
      self.BoardSize = size #the size of the board
      self.CurrentGameBoard= board #the current state of the game board

    def set_value(self, row, col, value):
        """This function will create a new sudoku board object with the input
        value placed on the GameBoard row and col are both zero-indexed"""

        #add the value to the appropriate position on the board
        self.CurrentGameBoard[row][col]=value
        #return a new board of the same size with the value added
        return SudokuBoard(self.BoardSize, self.CurrentGameBoard)


    def print_board(self):
        """Prints the current game board. Leaves unassigned spots blank."""
        div = int(math.sqrt(self.BoardSize))
        dash = ""
        space = ""
        line = "+"
        sep = "|"
        for i in range(div):
            dash += "----"
            space += "    "
        for i in range(div):
            line += dash + "+"
            sep += space + "|"
        for i in range(-1, self.BoardSize):
            if i != -1:
                print "|",
                for j in range(self.BoardSize):
                    if self.CurrentGameBoard[i][j] > 9:
                        print self.CurrentGameBoard[i][j],
                    elif self.CurrentGameBoard[i][j] > 0:
                        print "", self.CurrentGameBoard[i][j],
                    else:
                        print "  ",
                    if (j+1 != self.BoardSize):
                        if ((j+1)//div != j/div):
                            print "|",
                        else:
                            print "",
                    else:
                        print "|"
            if ((i+1)//div != i/div):
                print line
            else:
                print sep

def parse_file(filename):
    """Parses a sudoku text file into a BoardSize, and a 2d array which holds
    the value of each cell. Array elements holding a 0 are considered to be
    empty."""

    f = open(filename, 'r')
    BoardSize = int(f.readline())
    NumVals = int(f.readline())

    #initialize a blank board
    board = [[ 0 for i in range(BoardSize) ] for j in range(BoardSize) ]

    #populate the board with initial values
    for i in range(NumVals):
        line = f.readline()
        chars = line.split()
        row = int(chars[0])
        col = int(chars[1])
        val = int(chars[2])
        board[row-1][col-1]=val

    return board

def is_complete(sudoku_board):
    """Takes in a sudoku board and tests to see if it has been filled in
    correctly."""
    BoardArray = sudoku_board.CurrentGameBoard
    size = len(BoardArray)
    subsquare = int(math.sqrt(size))

    #check each cell on the board for a 0, or if the value of the cell
    #is present elsewhere within the same row, column, or square
    for row in range(size):
        for col in range(size):
            if BoardArray[row][col]==0:
                return False
            for i in range(size):
                if ((BoardArray[row][i] == BoardArray[row][col]) and i != col):
                    return False
                if ((BoardArray[i][col] == BoardArray[row][col]) and i != row):
                    return False
            #determine which square the cell is in
            SquareRow = row // subsquare
            SquareCol = col // subsquare
            for i in range(subsquare):
                for j in range(subsquare):
                    if((BoardArray[SquareRow*subsquare+i][SquareCol*subsquare+j]
                            == BoardArray[row][col])
                        and (SquareRow*subsquare + i != row)
                        and (SquareCol*subsquare + j != col)):
                            return False
    return True

def init_board(file_name):
    """Creates a SudokuBoard object initialized with values from a text file"""
    board = parse_file(file_name)
    return SudokuBoard(len(board), board)

# BOARD.py

class boardCell:
    """Holds the necessary information about a cell"""
    def __init__(self, BoardSize, value, section, row, column, fwd):
        self.cellVal = value
        self.possibleVals = set(range(1, BoardSize+1))
        self.boardSection = section
        self.row = row
        self.column = column
        self.constrainedCells = 3 * BoardSize - 2 * int(math.sqrt(BoardSize)) - 1

    def setCell(self, value):
        """Set cell value"""
        self.cellVal = value

    def removePossibleVal(self, value):
        """Removes specified value from set of possible values if present"""
        if value in self.possibleVals:
            self.possibleVals.remove(value)
            if self.cellVal == 0 and len(self.possibleVals) == 0:
                return False
        self.constrainedCells -= 1
        return True

class MyBoard:
    """Represents board w/ every cell a boardCell"""    
    def __init__(self, sb, bsize, fwd = True):
        """Inits board to blank, then calls addValue for each cell w/ specified value"""
        self.boardSize = bsize
        self.board = []
        self.squaresFilled = 0
        self.blankCells = []
        subsquare = int(math.sqrt(bsize))
        #Make empty board of cells with all 0's
        for i in range(0, bsize):
            self.board.append([])
            for j in range(0, bsize):
                boardCol = j // subsquare
                boardRow = i // subsquare
                boardSection =  boardRow * subsquare + boardCol
                cell = boardCell(bsize, 0, boardSection, i, j, fwd)
                self.board[i].append(cell)
                self.blankCells.append(cell)
        #Search through board of ints for non-zero values, and set board
        for i in range(0, bsize):
            for j in range(0, bsize):
                if sb[i][j] != 0:
                    self.addValue(sb[i][j], i, j, fwd)

    def addValue(self, value, row, col, fwd):
        """Set cell value"""    
        cell = self.board[row][col]
        cell.setCell(value)
        self.squaresFilled += 1
        self.blankCells.remove(cell)

        global globalcount
        globalcount += 1

        if fwd:   #If forward checking is on update the possible values of affected cells
            for i in range(self.boardSize):
                for j in range(self.boardSize):
                    if row == i and col == j:
                        continue
                    if self.board[i][j].boardSection == cell.boardSection:
                        if self.board[i][j].removePossibleVal(value) is False:
                            return False
                        continue
                    if i == cell.row and value in self.board[i][j].possibleVals:
                        if self.board[i][j].removePossibleVal(value) is False:
                            return False
                        continue
                    if j == cell.column and value in self.board[i][j].possibleVals:
                        if self.board[i][j].removePossibleVal(value) is False:
                            return False
            return True
        else:  #otherwise just check if the move you made messed with anything else
            return self.checkConsistent(cell)

    def removedValCount(self, tile, value):
        """Counts how many values are removed from possibleVals 
        in all cells if value is assigned to tile"""
        count = 0
        currentRow = tile.row
        currentColumn = tile.column
        currentSection = tile.boardSection

        for cell in self.blankCells:
            if cell.row == currentRow:
                if value in cell.possibleVals:
                    count += 1
                    continue
            if cell.column == currentColumn:
                if value in cell.possibleVals:
                    count += 1
                    continue
            if cell.boardSection == currentSection:
                if value in cell.possibleVals:
                    count += 1
        return count

    def checkComplete(self):
        """Checks if the board has been solved"""
        intBoard = []
        for i in range(self.boardSize):
            intBoard.append([])
            for j in range(self.boardSize):
                intBoard[i].append(self.board[i][j].cellVal)
        sboard = SudokuBoard(self.boardSize, intBoard)
        return is_complete(sboard)

    def isFull(self):
        """Checks if all squares are filled"""
        if self.squaresFilled == self.boardSize * self.boardSize:
            return True
        return False

    def checkConsistent(self, cell):
        """Checks if the board can possibly be solved"""
        currentVal = cell.cellVal
        currentRow = cell.row
        currentColumn = cell.column
        currentSection = cell.boardSection
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if currentRow == i and currentColumn == j:
                    continue
                if self.board[i][j].boardSection == currentSection:
                    if currentVal == self.board[i][j].cellVal:
                        return False
                if i == currentRow and currentVal == self.board[i][j].cellVal:
                    return False
                if j == currentColumn and currentVal == self.board[i][j].cellVal:
                    return False
        return True

    def print_board(self):
        """Translates our board class into initial board class and prints"""
        intBoard = []
        for i in range(self.boardSize):
            intBoard.append([])
            for j in range(self.boardSize):
                intBoard[i].append(self.board[i][j].cellVal)
        sboard = SudokuBoard(self.boardSize, intBoard)
        sboard.print_board()

# action.py

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


# solve

def solve(initial_board, forward_checking = False, MRV = False, MCV = False,
    LCV = False):
    """Required solver funciton"""
    mb = MyBoard(initial_board.CurrentGameBoard, initial_board.BoardSize, forward_checking)
    solvedBoard = sudokuSolve(mb, forward_checking, MRV, MCV, LCV)

    return solvedBoard


def t(fc, mrv, mcv, lcv):
    global globalcount
    globalcount = 0

    sb = init_board("input_puzzles/easy/4_4.sudoku")
    mb = solve(sb, fc, mrv, mcv, lcv)
    mb.print_board()
    print globalcount

    globalcount = 0
    sb = init_board("input_puzzles/easy/9_9.sudoku")
    mb = solve(sb, fc, mrv, mcv, lcv)
    mb.print_board()
    print globalcount

    globalcount = 0
    sb = init_board("input_puzzles/easy/16_16.sudoku")
    mb = solve(sb, fc, mrv, mcv, lcv)
    mb.print_board()
    print globalcount

    globalcount = 0
    sb = init_board("input_puzzles/easy/25_25.sudoku")
    mb = solve(sb, fc, mrv, mcv, lcv)
    mb.print_board()
    print globalcount