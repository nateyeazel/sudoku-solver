from action import *


def ttest():
    sb = parse_file("input_puzzles/easy/16_16.sudoku")
    m = MyBoard(sb, len(sb))
    m.p()
    b = sudokuSolve(m)
    b.p()
    return b


def boardTest(file):
    sb = parse_file(file)
    m = MyBoard(sb, len(sb))
    m.p()

def test(inputFile, fc, mrv, mcv, lcv):
    sb = init_board(inputFile)
    mb = solve(sb, fc, mrv, mcv, lcv)
    mb.print_board()
