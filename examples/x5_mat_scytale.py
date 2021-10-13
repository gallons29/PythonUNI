#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

text = ""
with open("p5_mat_scytale.py") as infile:
    text = infile.read()

with open("_output.txt", "w") as outfile:
    FILLER = ' '
    ROWS = 3
    COLS = 4

    matrix = [[' '] * COLS for y in range(ROWS)]
    i = 0
    while i < len(text):
        for y in range(ROWS):
            for x in range(COLS):
                if i < len(text):
                    matrix[y][x] = text[i]
                    i += 1
                else:
                    matrix[y][x] = FILLER

        for x in range(COLS):
            for y in range(ROWS):
                print(matrix[y][x], end="", file=outfile)
