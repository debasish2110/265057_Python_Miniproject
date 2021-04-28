# importing the dependencies
import os
import sys
from time import sleep


# The screen clear function
def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


# this function will print the cover page.... which is saved in the form of a text file
def view_coverpage():
    with open('src/cover_page.txt') as f:
        coverpage = f.read()
    print(coverpage)


# print board function will print the board
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
                # End of print_board function


# find_empty function will find the empty place(s)
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None
    # End of find_empty function


# this function checks the validity
def is_valid(bo, num, pos):
    for i in range(len(bo[0])):  # checking row
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    for j in range(len(bo)):  # checking column
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True
    # End of valid funtion


# this is the function which solves the sudoku puzzle
def solver(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if is_valid(bo, i, (row, col)):
            bo[row][col] = i
            if solver(bo):  # using recursion
                return True
            bo[row][col] = 0
    return False
    # end of solver function


# board1 board2 board3  are 3 different types of lists that contains lists of the numbers in sudoku....

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


# this function solves the easy board
def solve_easy():
    print_board(board_easy)
    solver(board_easy)
    print("\n\n\n")
    print('\x1b[0;33;40m' + "=============================" + "Solving" + "=============================" + '\x1b[0m')
    print("\n\n")
    print_board(board_easy)
    print("\n")
    print('\x1b[1;32;40m' + "=============================" + "Solved" + "=============================" + '\x1b[0m')
    print("\n\n")
    # end of function


# this function solves the medium board
def solve_mid():
    print_board(board_mid)
    solver(board_mid)
    print("\n")
    print('\x1b[0;33;40m' + "=============================" + "Solving" + "=============================" + '\x1b[0m')
    print("\n\n")
    print_board(board_mid)
    print("\n")
    print('\x1b[1;32;40m' + "=============================" + "Solved" + "=============================" + '\x1b[0m')
    print("\n\n")
    # end of function


# this function solves the hard board
def solve_hard():
    print_board(board_hard)
    solver(board_hard)
    print("\n")
    print('\x1b[0;33;40m' + "=============================" + "Solving" + "=============================" + '\x1b[0m')
    print("\n\n")
    print_board(board_hard)
    print("\n")
    print('\x1b[1;32;40m' + "=============================" + "Solved" + "=============================" + '\x1b[0m')
    print("\n\n")
    # end of function


# this function solves the very hard board
def solve_very_hard():
    print_board(board_very_hard)
    solver(board_very_hard)
    print("\n")
    print('\x1b[0;33;40m' + "=============================" + "Solving" + "=============================" + '\x1b[0m')
    print("\n\n")
    print_board(board_very_hard)
    print("\n")
    print('\x1b[1;32;40m' + "=============================" + "Solved" + "=============================" + '\x1b[0m')
    print("\n\n")
    # end of function


def default():
    return "Please enter a valid Difficulty level... :("


# this function prints the options which are written in the difficulty_level_choice.txt file inside src folder
def view_options():
    with open('src/difficulty_level_choice.txt') as f:
        options = f.read()
    print(options)
    # end of function


if __name__ == '__main__':
    # taking the difficult level choice from the user
    view_coverpage()
    print("""
    Enter 1 to Continue...
    Enter 0 to exit...
    """)

    ip = int(input("enter ur choice(either 1 or 2): "))
    sleep(1)
    screen_clear()

    if ip == 1:
        view_options()
        choice = int(input("Enter The Difficulty Level: "))
        sleep(1)
        screen_clear()
        print("\n\n")

        # using switcher to mimic the switch cse statement
        switcher = {
            1: solve_easy,
            2: solve_mid,
            3: solve_hard,
            4: solve_very_hard
        }
        switcher.get(choice, default)()  # calling the function acc to ip given by the user
    else:
        sys.exit("\n\nThank You... _/\_ visit again... \n")

"""
Assignment submitted by Debashish Dash (265057)
"""
