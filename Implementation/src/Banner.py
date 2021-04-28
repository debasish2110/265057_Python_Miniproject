
"""
This file prints the banner in to a text file and that text file is further used in the main code
"""

import pyfiglet
from termcolor import colored

# print(pyfiglet. FigletFont.getFonts())

word = colored(pyfiglet.figlet_format("""
WELCOME
TO
SUDOKU SOLVER
""", font='banner3-D'), 'blue')

# writing the banner in the coverpage file
with open('cover_page.txt', 'w') as fw:
    fw.write(word)

with open('cover_page.txt') as f:
    options = f.read()
print(options)
