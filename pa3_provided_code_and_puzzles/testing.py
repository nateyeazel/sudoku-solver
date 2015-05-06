from crb331 import *
import time


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
    startTime = time.time()
    mb = solve(sb, fc, mrv, mcv, lcv)
    mb.print_board()
    timeLength = time.time() - startTime
    print "It took: ", timeLength, " seconds to solve."

def testAllFiles(fc, mrv, mcv, lcv):
    test9Files(fc, mrv, mcv, lcv)
    test16Files(fc, mrv, mcv, lcv)
    test25Files(fc, mrv, mcv, lcv)

def test9Files(fc, mrv, mcv, lcv):
    totalTime = 0
    print "\nNow testing 9x9 files:"
    for i in range (1, 21):
        inputFile = "input_puzzles/more/9x9/9x9.{num}.sudoku".format(num = i)
        sb = init_board(inputFile)
        startTime = time.time()
        mb = solve(sb, fc, mrv, mcv, lcv)
        timeLength = time.time() - startTime
        totalTime += timeLength
        print "Solved board ", i, " in ", timeLength, " seconds"
    print "It took: ", totalTime, " seconds total.\n"

def test16Files(fc, mrv, mcv, lcv):
    totalTime = 0
    print "\nNow testing 16x16 files:"
    for i in range (1, 21):
        inputFile = "input_puzzles/more/16x16/16x16.{num}.sudoku".format(num = i)
        sb = init_board(inputFile)
        startTime = time.time()
        mb = solve(sb, fc, mrv, mcv, lcv)
        timeLength = time.time() - startTime
        totalTime += timeLength
        print "Solved board ", i, " in ", timeLength, " seconds"
    print "It took: ", totalTime, " seconds total.\n"

def test25Files(fc, mrv, mcv, lcv):
    totalTime = 0
    print "\nNow testing 25x25 files:"
    for i in range (1, 21):
        inputFile = "input_puzzles/more/25x25/25x25.{num}.sudoku".format(num = i)
        sb = init_board(inputFile)
        startTime = time.time()
        mb = solve(sb, fc, mrv, mcv, lcv)
        timeLength = time.time() - startTime
        totalTime += timeLength
        print "Solved board ", i, " in ", timeLength, " seconds"
    print "It took: ", totalTime, " seconds total.\n"

# def t(fc, mrv, mcv, lcv):

#     sb = init_board("input_puzzles/easy/4_4.sudoku")
#     mb = solve(sb, fc, mrv, mcv, lcv)
#     mb.print_board()
#     print globalcount

#     # globalcount = 0
#     sb = init_board("input_puzzles/easy/9_9.sudoku")
#     mb = solve(sb, fc, mrv, mcv, lcv)
#     mb.print_board()
#     print globalcount

#     # globalcount = 0
#     sb = init_board("input_puzzles/easy/16_16.sudoku")
#     mb = solve(sb, fc, mrv, mcv, lcv)
#     mb.print_board()
#     print globalcount

#     # globalcount = 0
#     sb = init_board("input_puzzles/easy/25_25.sudoku")
#     mb = solve(sb, fc, mrv, mcv, lcv)
#     mb.print_board()
#     print globalcount