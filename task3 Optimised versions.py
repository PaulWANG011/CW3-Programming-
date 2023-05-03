# -*- coding: utf-8 -*-
"""
Created on Wed May  3 03:04:20 2023

@author: Windows11
"""
import pprint
grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

def check_solution(grid):
    # Check if the Sudoku grid has any empty cells left
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if type(grid[i][j]) == list:
                return False
    return True

def the_missing_numbers(grid, n_cols, n_rows, which_row, which_column):
    '''
    This function returns the possible numbers that can be added to an empty cell in the Sudoku grid.
    grid - the grid we need to solve.
    n_cols, n_rows - the number of columns and rows in each square in the grid.
    which_row, which_column - the row and column position of the empty cell.

    It will be called in the `find_empty` function to select the empty location with the fewest number of variable options to fill.
    '''
    numbers_list = []  # list to collect numbers that cannot be added to the empty (0)
    
    # Collecting numbers in the same square
    for i in range(n_cols):
        rows = (i * n_rows, (i + 1) * n_rows)
        for j in range(n_rows):
            columns = (j * n_cols, (j + 1) * n_cols)
            square = []
            for k in range(rows[0], rows[1]):
                line = grid[k][columns[0]:columns[1]]
                square += line
            if which_column in range(columns[0], columns[1]) and which_row in range(rows[0], rows[1]):
                for num in square:
                    if num != 0 and type(num) != list:
                        numbers_list.append(num)  # add the numbers of the square

    # Collecting numbers in the same row
    for num in grid[which_row]:
        if num != 0 and type(num) != list:
            numbers_list.append(num)  # add the numbers in the row

    # Collecting numbers in the same column
    for i in range(0, n_cols * n_rows):
        column_num = grid[i][which_column]
        if column_num != 0 and type(column_num) != list:
            numbers_list.append(column_num)  # add the numbers in the same column

    # All numbers that can be added to the Sudoku
    all_numbers = [*range(1, n_cols * n_rows + 1)]
    all_numbers = set(all_numbers)

    # Possible numbers that can be added to the empty cell (0)
    possible_numbers = all_numbers.symmetric_difference(set(numbers_list))

    return list(possible_numbers)


def add_lists(grid, n_cols, n_rows):
    '''
    This function adds the possible numbers to the empty cells (0) in the Sudoku grid.
    grid - the grid we need to solve.
    n_cols, n_rows - the number of columns and rows in each square in the grid.

    Returns the updated grid.
    '''
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if grid[i][j] == 0:
                b = the_missing_numbers(grid, n_cols, n_rows, i, j)
                if len(b) == 1: # if there is only one possible number to add
                    grid[i][j] = b[0] # fill in the cell with that number
    return grid


def fill_in(grid):
    '''
    This function fills in a number if there is only one possible number to add in an empty cell.
    grid - the grid we need to solve.

    Returns a list containing the updated grid, the row and column positions of the cell that was filled in.
    '''
    updated_cell = None # initialize updated cell to None
    while True:
        filled_in = False # set filled_in flag to False
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    b = the_missing_numbers(grid, 3, 3, i, j)
                    if len(b) == 1:
                        grid[i][j] = b[0]
                        filled_in = True # set filled_in flag to True
                        updated_cell = (i, j) # update updated_cell
        if not filled_in: # if no cells were filled in the last iteration
            break # exit the loop
    return [grid, updated_cell]
solution = fill_in(grid)
pprint.pprint(solution)