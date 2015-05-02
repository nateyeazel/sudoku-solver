from SudokuStarter import *

class boardCell:
    """Holds the necessary information about a cell"""
    def __init__(self, BoardSize, value, section, row, column, fwd):
        self.cellVal = value
        if fwd:
            self.possibleVals = set(range(1, BoardSize+1))
        self.boardSection = section
        self.row = row
        self.column = column
        self.constrainedCells = 3 * BoardSize - 2 * int(math.sqrt(BoardSize)) - 1

    def setCell(self, value):
        self.cellVal = value

    def removePossibleVal(self, value):
        if value in self.possibleVals:
            self.possibleVals.remove(value)
            if self.cellVal == 0 and len(self.possibleVals) == 0:
                return False
        self.constrainedCells -= 1
        return True

class MyBoard:
    def __init__(self, sb, bsize, fwd = True):
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
        cell = self.board[row][col]
        cell.setCell(value)
        self.squaresFilled += 1
        self.blankCells.remove(cell)

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

    def removeValCount(self, tile, value):
        count = 0
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if tile.row == i and tile.column == j:
                    continue
                if self.board[i][j].boardSection == tile.boardSection:
                    if value in self.board[i][j].possibleVals:
                        count += 1
                    continue
                if i == tile.row and value in self.board[i][j].possibleVals:
                    count +=1
                if j == tile.column and value in self.board[i][j].possibleVals:
                    count +=1
        return count

    def checkComplete(self):
        intBoard = []
        for i in range(self.boardSize):
            intBoard.append([])
            for j in range(self.boardSize):
                intBoard[i].append(self.board[i][j].cellVal)
        sboard = SudokuBoard(self.boardSize, intBoard)
        return is_complete(sboard)

    def isFull(self):
        if self.squaresFilled == self.boardSize * self.boardSize:
            return True
        return False

    def checkConsistent(self, cell):
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
