from SudokuStarter import *

class boardCell:
    """Holds the necessary information about a cell"""
    def __init__(self, BoardSize, value, section):
        self.cellVal = value
        self.possibleVals = set(range(1, BoardSize+1))
        self.previouslyTried = 0
        self.boardSection = section

    def setCell(self, value):
        self.cellVal = value

    def removePossibleVal(self, value):
        if value in self.possibleVals:
            self.possibleVals.remove(value)


class MyBoard:
    def __init__(self, sb, bsize):
        self.boardSize = bsize
        self.board = []
        subsquare = int(math.sqrt(bsize))
        #Make empty board of cells with all 0's
        for i in range(0, bsize):
            self.board.append([])
            for j in range(0, bsize):
                boardCol = j // subsquare
                boardRow = i // subsquare
                boardSection =  boardRow * subsquare + boardCol
                self.board[i].append(boardCell(bsize, 0, boardSection))
        #Search through board of ints for non-zero values, and set board
        for i in range(0, bsize):
            for j in range(0, bsize):
                if sb[i][j] != 0:
                    self.addValue(sb[i][j], i, j)

    def addValue(self, value, row, col):
        self.board[row][col].setCell(value)
        for i in range(self.boardSize):
            if i != col:
                self.board[row][i].removePossibleVal(value)
            if i != row:
                self.board[i][col].removePossibleVal(value)
        subsquareMates = self.getSubsquareMates(self.board[row][col])
        for tile in subsquareMates:
            tile.removePossibleVal(value)

    def getSubsquareMates(self, cell):
        currentSection = cell.boardSection
        subsquareMates = []
        for i in range(self.boardSize):
            for tile in self.board[i]:
                if tile.boardSection == currentSection:
                    subsquareMates.append(tile)
        return subsquareMates

    def checkComplete(self):
        intBoard = []
        for i in range(self.boardSize):
            intBoard.append([])
            for j in range(self.boardSize):
                intBoard[i].append(self.board[i][j].cellVal)
        sboard = SudokuBoard(self.boardSize, intBoard)
        return is_complete(sboard)

    def checkConsistent(self):
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                cell = self.board[i][j]
                if cell.cellVal == 0 and len(cell.possibleVals) == 0:
                    return False
        return True

    def p(self):
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if self.board[i][j].cellVal:
                    print self.board[i][j].cellVal
                else:
                    print "(" + str(self.board[i][j].possibleVals) + ")"
            print "\n"
