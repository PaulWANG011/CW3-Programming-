# -*- coding: utf-8 -*-
"""
Created on Mon May  1 16:40:30 2023

@author: MCDONALD
"""

def print_grid(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")
def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)  # row, col
    return None
def is_valid(grid, n, row, col):
    # Check row
    for i in range(len(grid[0])):
        if grid[row][i] == n and col != i:
            return False
    # Check column
    for i in range(len(grid)):
        if grid[i][col] == n and row != i:
            return False
    # Check box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if grid[i][j] == n and (i, j) != (row, col):
                return False
    return True
def solve_grid(grid):
    find = find_empty(grid)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(grid, i, row, col):
            grid[row][col] = i

            if solve_grid(grid):
                return True

            grid[row][col] = 0

    return False

grid = [
    [1, 0, 5, 0, 4, 0, 0, 3, 0],
    [0, 6, 0, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 3, 1, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 6, 0, 9],
    [3, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 0, 0, 0]
]

solve_grid(grid)
print_grid(grid)


