# import time
# import pygame as pg
# import sys
# from grid import grid
# # Backtracking algorithm
# # Run this file to see the backtracking algorithm in action
    

# Solve function
def solve(g):
    find = find_empty(g)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(g, i, (row, col)):
            g[row][col]["num"] = i
            if solve(g):
                return True

            g[row][col]["num"] = None

    return False


# Check if valid
def valid(g, num, pos):
    # Check row
    for i in range(len(g[pos[0]])):
        if g[pos[0]][i]["num"] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(g)):
        if g[i][pos[1]]["num"] == num and pos[0] != i:
            return False

    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if g[i][j]["num"] == num and (i, j) != pos:
                return False
    return True


# Find an empty cell
def find_empty(g):
    for row in range(len(g)):
        for col in range(len(g[row])):
            if g[row][col]["num"] == None:
                return (row, col)  # This is the position of the empty cell


solve(grid)
