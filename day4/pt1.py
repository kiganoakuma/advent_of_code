import sys
import re

def create_board(row_list):
    grid = {}
    for r in range(len(row_list)):
        row = row_list[r]
        for c in range(len(row)):
            grid[f'{r}, {c}'] = row_list[r][c]
    return grid


def get_matches(y, x, dict, found, row_list):
    found_c = found.copy()
    if y - 3 >= 0 and x - 3 >= 0:
        tl = dict[f'{y}, {x}'] +  dict[f'{y - 1}, {x - 1}'] + dict[f'{y - 2}, {x - 2}'] + dict[f'{y - 3}, {x - 3}']  
        tlc = f'{y}, {x} - {y - 3}, {x - 3}'
        if tl == 'XMAS':
            found_c[tlc] = tl

    if y - 3 >= 0:
        t = dict[f'{y}, {x}'] +  dict[f'{y - 1}, {x}'] + dict[f'{y - 2}, {x}'] + dict[f'{y - 3}, {x}']  
        tc = f'{y}, {x} - {y - 3}, {x}'
        if t == 'XMAS':
            found_c[tc] = t

    if y - 3 >= 0 and x + 3 <= len(row_list[0]) - 1:
        tr = dict[f'{y}, {x}'] +  dict[f'{y - 1}, {x + 1}'] + dict[f'{y - 2}, {x + 2}'] + dict[f'{y - 3}, {x + 3}']  
        trc = f'{y}, {x} - {y - 3}, {x + 3}'
        if tr == 'XMAS':
            found_c[trc] = tr

    if x - 3 >= 0:
        cl = dict[f'{y}, {x}'] +  dict[f'{y}, {x - 1}'] + dict[f'{y}, {x - 2}'] + dict[f'{y}, {x - 3}']  
        clc = f'{y}, {x} - {y}, {x - 3}'
        if cl == 'XMAS':
            found_c[clc] = cl


    if x + 3 <= len(row_list[0]) - 1:
        cr = dict[f'{y}, {x}'] +  dict[f'{y}, {x + 1}'] + dict[f'{y}, {x + 2}'] + dict[f'{y}, {x + 3}']  
        crc = f'{y}, {x} - {y}, {x + 3}'
        if cr == 'XMAS':
            found_c[crc] = cr

    if y + 3 <= len(row_list) - 1 and x - 3 >= 0:
        bl = dict[f'{y}, {x}'] +  dict[f'{y + 1}, {x - 1}'] + dict[f'{y + 2}, {x - 2}'] + dict[f'{y + 3}, {x - 3}']  
        blc = f'{y}, {x} - {y + 3}, {x - 3}'
        if bl == 'XMAS':
            found_c[blc] = bl

    if y + 3 <= len(row_list) - 1:
        b = dict[f'{y}, {x}'] +  dict[f'{y + 1}, {x}'] + dict[f'{y + 2}, {x}'] + dict[f'{y + 3}, {x}']  
        bc = f'{y}, {x} - {y + 3}, {x}'
        if b == 'XMAS':
            found_c[bc] = b

    if y + 3 <= len(row_list) - 1 and x + 3 <= len(row_list[0]) - 1:
        br = dict[f'{y}, {x}'] +  dict[f'{y + 1}, {x + 1}'] + dict[f'{y + 2}, {x + 2}'] + dict[f'{y + 3}, {x + 3}']  
        brc = f'{y}, {x} - {y + 3}, {x + 3}'
        if br == 'XMAS':
            found_c[brc] = br

    return found_c
    
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
found_matches = {}
target = 'xmas'
current_found = ['X']
for key in board:
    y, x = map(int, re.findall(r'[0-9]+', key))
    found_matches = get_matches(y, x, board, found_matches, lines)

print(len(found_matches))
