from action import *


def btrackTest():
    sb = parse_file("input_puzzles/easy/4_4.sudoku")
    m = MyBoard(sb, len(sb))
    b = backTracking(m)
    b.p()
    return b