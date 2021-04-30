import pytest

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

demo = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
]


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None


def test_find_empty():
    assert find_empty(demo) == None
