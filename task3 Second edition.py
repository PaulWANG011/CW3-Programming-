# -*- coding: utf-8 -*-
"""
Created on Tue May  2 21:32:28 2023

@author: Windows11
"""
def solve_sudoku(grid):
    """
    Solves a 9x9 Sudoku grid using the wavefront propagation algorithm with added X-wing, swordfish, and coloring techniques.

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

        # Check for hidden singles (values that only appear once in a row, column, or box)
        for row in range(9):
            if value in possible_values[row][j]:
                possible_values[row][j].remove(value)
                if len(possible_values[row][j]) == 1:
                    wavefront.append((row, j))
            if value in possible_values[i][row]:
                possible_values[i][row].remove(value)
                if len(possible_values[i][row]) == 1:
                    wavefront.append((i, row))
        box_i = (i // 3) * 3
        box_j = (j // 3) * 3
        for row in range(box_i, box_i + 3):
            for col in range(box_j, box_j + 3):
                if value in possible_values[row][col]:
                    possible_values[row][col].remove(value)
                    if len(possible_values[row][col]) == 1:
                        wavefront.append((row, col))

        # Check for X-wing and swordfish
        for digit in range(1, 10):
            rows = [i for i in range(9) if digit in possible_values[i][j]]
            cols = [j for j in range(9) if digit in possible_values[i][j]]
            if len(rows) == 2:
            # Check for X-wing
            col1, col2 = cols[0] // 3, cols[1] // 3
            if col1 == col2:
            for k in range(9):
            if k // 3 != col1 and digit in possible_values[rows[0]][k] and digit in possible_values[rows[1]][k]:
            possible_values[rows[0]][k].remove(digit)
            possible_values[rows[1]][k].remove(digit)
            if len(possible_values[rows[0]][k]) == 1:
            wavefront.append((rows[0], k))
            if len(possible_values[rows[1]][k]) == 1:
            wavefront.append((rows[1], k))
            elif len(rows) == 3:
            # Check for swordfish
            cols_set = set(cols)
            if len(cols_set) == 3:
            for k in range(9):
            if k not in cols_set and digit in possible_values[rows[0]][k] and digit in possible_values[rows[1]][k] and digit in possible_values[rows[2]][k]:
            possible_values[rows[0]][k].remove(digit)
            possible_values[rows[1]][k].remove(digit)
            possible_values[rows[2]][k].remove(digit)
            if len(possible_values[rows[0]][k]) == 1:
            wavefront.append((rows[0], k))
            if len(possible_values[rows[1]][k]) == 1:
            wavefront.append((rows[1], k))
            if len(possible_values[rows[2]][k]) == 1:
            wavefront.append((rows[2], k))
            # Check for coloring
    for color in range(2):
        for digit in range(1, 10):
            digits = [i for i in range(1, 10) if i != digit]
            cells = [(i, j) for i in range(9) for j in range(9) if digit in possible_values[i][j]]
            for cell in cells:
                row, col = cell
                for d in digits:
                    if d in possible_values[row][col]:
                        color_set = set()
                        for k in range(9):
                            if (row, k) in cells and d in possible_values[row][k]:
                                color_set.add(color)
                            if (k, col) in cells and d in possible_values[k][col]:
                                color_set.add(color)
                            box_i = (row // 3) * 3 + k // 3
                            box_j = (col // 3) * 3 + k % 3
                            if (box_i, box_j) in cells and d in possible_values[box_i][box_j]:
                                color_set.add(color)
                        if len(color_set) == 1:
                            possible_values[row][col] = set([digit])
                            wavefront.append(cell)
                            break

    # Check for solved puzzle
    if any(len(possible_values[i][j]) != 1 for i in range(9) for j in range(9)):
        continue
    else:
        return True, grid

return False, grid
