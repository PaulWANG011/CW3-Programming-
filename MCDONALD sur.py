# -*- coding: utf-8 -*-
"""
Created on Mon May  1 17:22:31 2023

@author: MCDONALD
"""
grid = [    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def solve_sudoku(grid):
    """
    Solves a 9x9 Sudoku grid using the wavefront propagation algorithm.

    Parameters:
    grid (list[list[int]]): a 9x9 grid of integers representing the Sudoku puzzle.
        Empty cells are represented by 0.

    Returns:
    A boolean value indicating if the Sudoku was solved successfully, and the solved grid.
    """
    # Define the possible values for each cell
    possible_values = [[set(range(1, 10)) for _ in range(9)] for _ in range(9)]

    # Initialize the wavefront with the known values in the grid
    wavefront = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                possible_values[i][j] = set([grid[i][j]])
                wavefront.append((i, j))

    # Propagate the constraints until there are no more changes
    while wavefront:
        i, j = wavefront.pop(0)
        value = possible_values[i][j].pop()

        # Update possible values for the row, column, and box
        for k in range(9):
            if value in possible_values[i][k]:
                possible_values[i][k].remove(value)
                if len(possible_values[i][k]) == 1:
                    wavefront.append((i, k))
            if value in possible_values[k][j]:
                possible_values[k][j].remove(value)
                if len(possible_values[k][j]) == 1:
                    wavefront.append((k, j))
            box_i = (i // 3) * 3 + k // 3
            box_j = (j // 3) * 3 + k % 3
            if value in possible_values[box_i][box_j]:
                possible_values[box_i][box_j].remove(value)
                if len(possible_values[box_i][box_j]) == 1:
                    wavefront.append((box_i, box_j))

        # Set the value in the grid
        grid[i][j] = value

    # Check if the Sudoku is solved
    for i in range(9):
        row = set(grid[i])
        if 0 in row:
            return False, grid
        if len(row) != 9:
            return False, grid
        col = set([grid[k][i] for k in range(9)])
        if len(col) != 9:
            return False, grid
        box_i = (i // 3) * 3
        box_j = (i % 3) * 3
        box = set([grid[box_i + k // 3][box_j + k % 3] for k in range(9)])
        if len(box) != 9:
            return False, grid

    return True, grid

success, solved_grid = solve_sudoku(grid)
print(success)
print(solved_grid)