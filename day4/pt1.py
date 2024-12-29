import sys
import re

def create_board(row_list):
    grid = {}
    for r in range(len(row_list)):
        row = row_list[r]
        for c in range(len(row)):
            grid[f'{r}, {c}'] = row_list[r][c]
    return grid

def get_surrounding(y, x, row_list):
    top = [
            (y - 1), (x - 1),
            (y - 1), (x),
            (y - 1), (x + 1),
        ]
    center = [
            (y), (x - 1),
            (y), (x + 1),
            ]
    bottom = [
            (y + 1), (x - 1),
            (y + 1), (x),
            (y + 1), (x + 1),
            ]
    if y == 0:
        # ignore top
        squares = [center, bottom]
        pass
    elif y == len(row_list):
        # ignore bottom
        squares = [top, center]
        pass
    else: 
        squares = [top, center, bottom]
   
    return squares


if len(sys.argv) > 1:
    file_inp = sys.argv[1]
else:
    raise Exception("please provide a filename")

with open(file_inp, 'r') as file:
    lines = []
    for line in file:
        letters = list(line.strip())
        lines.append(letters)


board = create_board(lines)    

for key in board:
    y, x = re.findall(r'[0-9]+', key)
    print(check_surrounding(int(x), int(y), board))
