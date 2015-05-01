from action import *


def ttest():
    sb = parse_file("input_puzzles/more/25x25/25x25.17.sudoku")
    m = MyBoard(sb, len(sb))
    b = sudokuSolve(m)
    b.p()
    return b


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
