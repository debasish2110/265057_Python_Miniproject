import pytest
import sys

sys.path.insert(1, "../")

board_notnull = [
    [3, 2, 4, 1, 5, 7, 6, 8, 9],
    [1, 5, 6, 2, 8, 9, 4, 7, 3],
    [9, 8, 7, 3, 4, 6, 1, 5, 2],
    [1, 7, 9, 3, 6, 4, 8, 2, 5],
    [8, 3, 6, 9, 2, 5, 7, 4, 1],
    [2, 4, 5, 1, 8, 7, 3, 6, 9],
    [3, 4, 8, 1, 5, 7, 2, 9, 6],
    [2, 6, 7, 4, 9, 8, 1, 3, 5],
    [5, 9, 1, 2, 3, 6, 7, 8, 4]
]

board_easy = [  # easy level sudoku
    [0, 2, 0, 1, 5, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0, 7, 0],
    [9, 8, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 3, 0, 4, 8, 0, 0],
    [8, 3, 6, 9, 2, 0, 7, 4, 1],
    [0, 4, 0, 0, 0, 7, 3, 6, 9],
    [0, 0, 0, 0, 0, 0, 2, 0, 6],
    [0, 0, 0, 4, 9, 8, 0, 0, 0],
    [5, 0, 1, 0, 0, 0, 0, 0, 4]
]

board_mid = [  # mid level sudoku
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

board_hard = [  # Hard level sudoku
    [0, 0, 0, 8, 0, 0, 6, 9, 3],
    [0, 8, 1, 3, 0, 0, 0, 0, 5],
    [0, 0, 0, 6, 0, 5, 4, 0, 0],
    [9, 0, 0, 0, 0, 0, 8, 5, 6],
    [8, 0, 0, 1, 0, 0, 0, 4, 0],
    [4, 0, 0, 5, 9, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 8, 0],
    [0, 5, 0, 0, 0, 0, 3, 6, 9],
    [0, 0, 0, 9, 2, 0, 0, 7, 0]
]

board_very_hard = [  # very hard level sudoku
    [0, 0, 7, 0, 0, 0, 9, 0, 0],
    [0, 0, 0, 0, 1, 0, 4, 7, 2],
    [0, 0, 4, 0, 8, 0, 0, 0, 0],
    [0, 6, 0, 9, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 9, 0, 6, 0, 3, 0, 0, 0],
    [1, 0, 0, 7, 0, 8, 0, 0, 0],
    [7, 0, 0, 0, 0, 6, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 8, 5]
]


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None


def test_find_empty():
    assert find_empty(board_notnull) is None  # test case 1
    assert find_empty(board_easy) is not None  # test case 2
    assert find_empty(board_mid) is not None  # test case 3
    assert find_empty(board_hard) is not None  # test case 4
    assert find_empty(board_very_hard) is not None  # test case 5
