from SudokuStarter import *

class boardCell:
    """Holds the necessary information about a cell"""
    def __init__(self, BoardSize, value, section, row, column):
        self.cellVal = value
        self.possibleVals = set(range(1, BoardSize+1))
        self.previouslyTried = 0
        self.boardSection = section
        self.row = row
        self.column = column

    def setCell(self, value):
        self.cellVal = value

    def removePossibleVal(self, value):
        if value in self.possibleVals:
            self.possibleVals.remove(value)
            if self.cellVal == 0 and len(self.possibleVals) == 0:
                return False
        return True

class MyBoard:
    def __init__(self, sb, bsize):
        self.boardSize = bsize
        self.board = []
        subsquare = int(math.sqrt(bsize))
        self.squaresFilled = 0
        self.firstBlankRow = 0
        self.firstBlankColumn = 0
        self.minRemainingValues = []
        #Make empty board of cells with all 0's
        for i in range(0, bsize):
            self.board.append([])
            for j in range(0, bsize):
                boardCol = j // subsquare
                boardRow = i // subsquare
                boardSection =  boardRow * subsquare + boardCol
                self.board[i].append(boardCell(bsize, 0, boardSection, i, j))
        #Search through board of ints for non-zero values, and set board
        for i in range(0, bsize):
            for j in range(0, bsize):
                if sb[i][j] != 0:
                    self.addValue(sb[i][j], i, j, True)

    def addValue(self, value, row, col, fwd):
        tile = self.board[row][col]
        tile.setCell(value)
        self.squaresFilled += 1

        if tile in self.minRemainingValues:
            self.minRemainingValues.remove(tile)

        if row == self.firstBlankRow and col == self.firstBlankColumn:
            self.updateFirstBlank(row, col)
        if fwd:  #update the possible values of affected tiles
            for i in range(self.boardSize):
                for j in range(self.boardSize):
                    if row == i and col == j:
                        continue
                    if self.board[i][j].boardSection == tile.boardSection:
                        if self.board[i][j].removePossibleVal(value) is False:
                            return False
                        continue
                    if i == tile.row and value in self.board[i][j].possibleVals:
                        if self.board[i][j].removePossibleVal(value) is False:
                            return False
                        continue
                    if j == tile.column and value in self.board[i][j].possibleVals:
                        if self.board[i][j].removePossibleVal(value) is False:
                            return False
        return True

    def updateFirstBlank(self, row, col):
        #This function finds the first empty square starting in the top left
        for i in range(col, self.boardSize):  #check the rest of the current row
            if self.board[row][i].cellVal == 0:
                self.firstBlankRow = row
                self.firstBlankColumn = i
                return
        for i in range(row, self.boardSize):
            for j in range(self.boardSize):
                if self.board[i][j].cellVal == 0:
                    self.firstBlankRow = i
                    self.firstBlankColumn = j
                    return

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

    def findMinimumRemainingValues(self):
        print "MIN REMAINING VALUES CALLED"
        minRemain = float("inf")
        for i in range(self.boardSize):
                for j in range(self.boardSize):
                    cell = self.board[i][j]
                    if cell.cellVal == 0:
                        if len(cell.possibleVals) < minRemain:
                            self.minRemainingValues = [cell]
                        if len(cell.possibleVals) == minRemain:
                            self.minRemainingValues.append(cell)

    def getAffectedCells(self, cell):
        cellList = []
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                cell = self.board[i][j]
                if cell.boardSection == section and cell.cellVal == 0:
                    cellList.append(cell)
                    continue
                if board.board[i][column].cellVal == 0 and i != row:
                    cellList.append(cell)
                    continue
                if board.board[row][i].cellVal == 0 and i != column:
                    cellList.append(cell)
        return cellList

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



    # def checkConsistent(self, tile, typ):
    #     if typ == "FWD":
    #         for i in range(self.boardSize):
    #             for j in range(self.boardSize):
    #                 cell = self.board[i][j]
    #                 if cell.cellVal == 0 and len(cell.possibleVals) == 0:
    #                     return False
    #         return True
    #     else:
    #         currentVal = tile.cellVal
    #         currentRow = tile.row
    #         currentColumn = tile.column
    #         currentSection = tile.boardSection
    #         for i in range(self.boardSize):
    #             if self.board[i][currentColumn].cellVal == currentVal and i != currentRow:
    #                 return False
    #             if self.board[currentRow][i].cellVal == currentVal and i != currentColumn:
    #                 return False
    #         for i in range(self.boardSize):
    #             for j in range(self.boardSize):
    #                 cell = self.board[i][j]
    #                 if i == currentRow and j == currentColumn:
    #                     continue
    #                 if cell.boardSection == currentSection and cell.cellVal == currentVal:
    #                     return False
    #         return True


    def p(self):
        print "============NEW Board====================="
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if self.board[i][j].cellVal:
                    print self.board[i][j].cellVal
                else:
                    print "(" + str(self.board[i][j].possibleVals) + ")"
            print "\n"
