import random
import copy
import time
import math
import argparse
from matplotlib import pyplot as plt
import trytask1 as t

# Grids 1-4 are 2x2
grid1 = [
    [1, 0, 4, 2],
    [4, 2, 1, 3],
    [2, 1, 3, 4],
    [3, 4, 2, 1]]

grid2 = [
    [1, 0, 4, 2],
    [4, 2, 1, 3],
    [2, 1, 0, 4],
    [3, 4, 2, 1]]

grid3 = [
    [1, 0, 4, 2],
    [4, 2, 1, 0],
    [2, 1, 0, 4],
    [0, 4, 2, 1]]

grid4 = [
    [1, 0, 4, 2],
    [0, 2, 1, 0],
    [2, 1, 0, 4],
    [0, 4, 2, 1]]

grid5 = [
    [1, 0, 0, 2],
    [0, 0, 1, 0],
    [0, 1, 0, 4],
    [0, 0, 0, 1]]

grid6 = [
    [0, 0, 6, 0, 0, 3],
    [5, 0, 0, 0, 0, 0],
    [0, 1, 3, 4, 0, 0],
    [0, 0, 0, 0, 0, 6],
    [0, 0, 1, 0, 0, 0],
    [0, 5, 0, 0, 6, 4]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2), (grid6, 2, 3)]
'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-explain', action='store_true', help='print out the answer')
    parser.add_argument('-file', nargs=2, default=None, help='input and output file names')
    parser.add_argument('-hint', type=int, default=None, help='return a grid with N values filled in')
    parser.add_argument('-profile', action='store_true', help='measures the performance of your solver(s)(in terms of time) for grids of different size')
    return parser.parse_args()

def get_solution_hint(grid, steps, hint):
    """
    get the solution based on @hint
    """
    steps_count = min(len(steps), hint)
    for step_idx in range(steps_count):
        step = steps[step_idx]
        grid[step[0]][step[1]] = step[2]
    return grid

def writelist(alist, f):
    """
    write a list to a file
    """
    for item in alist:
        f.write(str(item) + '\n')

def check_section(section, n):
    if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n + 1)]):
        return True
    return False


def get_squares(grid, n_rows, n_cols):
    squares = []
    for i in range(n_cols):
        rows = (i * n_rows, (i + 1) * n_rows)
        for j in range(n_rows):
            cols = (j * n_cols, (j + 1) * n_cols)
            square = []
            for k in range(rows[0], rows[1]):
                line = grid[k][cols[0]:cols[1]]
                square += line
            squares.append(square)

    return squares


# To complete the first assignment, please write the code for the following function
def check_solution(grid, n_rows, n_cols):
    '''
 This function is used to check whether a sudoku board has been correctly solved
 args: grid - representation of a suduko board as a nested list.
 returns: True (correct solution) or False (incorrect solution)
 '''
    n = n_rows * n_cols

    for row in grid:
        if check_section(row, n) == False:
            return False

    for i in range(n_rows ** 2):
        column = []
        for row in grid:
            column.append(row[i])

        if check_section(column, n) == False:
            return False

    squares = get_squares(grid, n_rows, n_cols)
    for square in squares:
        if check_section(square, n) == False:
            return False

    return True


def the_amount_of_numbers(grid, n_cols, n_rows, which_row, which_coulm):
    '''the arguemnts are grid=the grid we need to solve,
    n_cols and n_rows=the number of colums and rows in each sequare in the grid,
     which_eow and which_coulm= the colum and row the 0 in(location of 0),
    this function will be called in find empty function to select the empty location with the fewest number of variable options to fill'''
    numbers_list = []
    for i in range(n_cols):
        rows = (i * n_rows, (i + 1) * n_rows)
        for j in range(n_rows):
            cols = (j * n_cols, (j + 1) * n_cols)
            square = []
            for k in range(rows[0], rows[1]):
                line = grid[k][cols[0]:cols[1]]
                square += line
            if which_coulm in range(cols[0], cols[1]) and which_row in range(rows[0], rows[1]):
                for i in square:
                    if i !=0:
                        numbers_list.append(i)  # add the numbers of the square
    for i in grid[which_row]:
        if i != 0:
            numbers_list.append(i)  # add the numbers in the row
    for i in range(0, n_cols * n_rows):
        colum_number = grid[i][which_coulm]
        if colum_number!=0:
            numbers_list.append(colum_number)  # add the numbers in the same colum

    return list(set(numbers_list)) # calculate the amount of numbers that can not be replaced by the zero


def find_empty(grid, n_col, n_row):
    '''
 This function returns the index (i, j) to the feweist posibilities zero element in a sudoku grid
 If no such element is found, it returns None
 args: grid
 return: A tuple (i,j) where i and j are both integers, or None
 '''
    for i in range(len(grid)):
        row = grid[i]

        for j in range(len(row)):
            if grid[i][j] == 0:
                if len(the_amount_of_numbers(grid, n_col, n_row, i, j))==n_row*n_col-1:
                    return (i, j)
    for i in range(len(grid)):
        row = grid[i]

        for j in range(len(row)):
            if grid[i][j] == 0:
                return (i,j)
    return None


def recursive_solve(grid, n_rows, n_cols, steps):
    '''
 This function uses recursion to exhaustively search all possible solutions to a grid
 until the solution is found
 args: grid, n_rows, n_cols
 return: 
    A solved grid (as a nested list), or None
    the paths of the recursion
 '''

    # N is the maximum integer considered in this board
    n = n_rows * n_cols
    # Find an empty place in the grid
    empty = find_empty(grid, n_cols, n_rows)

    # If there's no empty places left, check if we've found a solution
    if not empty:
        # If the solution is correct, return it.
        if check_solution(grid, n_rows, n_cols):
            return grid, steps
        else:
            # If the solution is incorrect, return None
            return None, None
    else:
        row, col = empty

    # Loop through possible values
    for i in range(1, n + 1):
        if i not in the_amount_of_numbers(grid,n_cols,n_rows,row,col):
        # Place the value into the grid
            grid[row][col] = i
        # Recursively solve the grid
            ans_grid, ans_steps = recursive_solve(grid, n_rows, n_cols, steps + [[row, col, i]])
        # If we've found a solution, return it
            if ans_grid:
                return ans_grid, ans_steps

        # If we couldn't find a solution, that must mean this value is incorrect.
        # Reset the grid for the next iteration of the loop
        grid[row][col] = 0

    # If we get here, we've tried all possible values. Return none to indicate the previous value is incorrect.
    return None, None


def random_solve(grid, n_rows, n_cols, max_tries=50000):
   

    for i in range(max_tries):
        possible_solution = fill_board_randomly(grid, n_rows, n_cols)
        if check_solution(possible_solution, n_rows, n_cols):
            return possible_solution

    return grid


def fill_board_randomly(grid, n_rows, n_cols):
    '''
 This function will fill an unsolved Sudoku grid with random numbers
 args: grid, n_rows, n_cols
 return: A grid with all empty values filled in
 '''
    n = n_rows * n_cols
    # Make a copy of the original grid
    filled_grid = copy.deepcopy(grid)

    # Loop through the rows
    for i in range(len(grid)):
        # Loop through the columns
        for j in range(len(grid[0])):
            # If we find a zero, fill it in with a random integer
            if grid[i][j] == 0:
                filled_grid[i][j] = random.randint(1, n)

    return filled_grid


def solve(grid, n_rows, n_cols):
  

    #return random_solve(grid, n_rows, n_cols)
    return recursive_solve(grid, n_rows, n_cols, [])


'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''


def main():
    # parse args
    args = parse_args()
    hint = args.hint
    is_profile = args.profile
    is_explain = args.explain
    if args.file:
        input_file, output_file = args.file

    points = 0
    profile_time = {}

    if not args.file: 
        print("Running test script for coursework 1")
        print("====================================")
        for (i, (grid, n_rows, n_cols)) in enumerate(t.grids):
            grid_origin = copy.deepcopy(grid)
            print("Solving grid: %d" % (i + 1))
            start_time = time.time()
            solution, steps = solve(grid, n_rows, n_cols)
            elapsed_time = time.time() - start_time
            print("Solved in: %f seconds" % elapsed_time)
            profile_key = str((min(n_rows, n_cols), max(n_rows, n_cols)))
            if profile_key in profile_time:
                profile_time[profile_key].append(elapsed_time)
            else:
                profile_time[profile_key] = [elapsed_time]
            print("*** solution ***")
            if hint:
                print(get_solution_hint(grid_origin, steps, hint))
            else:
                print(solution)
            if is_explain:
                step_count = min(len(steps), hint) if hint else len(steps)
                print("*** steps ***")
                for step_idx in range(step_count):
                    step = steps[step_idx]
                    print("Put {step[2]} in location ({step[0]}, {step[1]})")
            if check_solution(solution, n_rows, n_cols):
                print("grid %d correct" % (i + 1))
                points = points + 10
            else:
                print("grid %d incorrect" % (i + 1))
        if is_profile:
            for key, value in profile_time.items():
                profile_time[key] = sum(value) / len(value)
            plt.bar(list(profile_time.keys()), profile_time.values(), width=0.3)
            plt.xlabel("Grid size")
            plt.ylabel("Average time (s)")
            plt.title("Average time taken to solve grids of different sizes")
            plt.show()

        print("====================================")
        print("Test script complete, Total points: %d" % points)
    else:
        with open(input_file, 'r') as f:
            lines = f.readlines()
        grids = []
        grid = []
        for line in lines:
            if line == '\n':
                grids.append((grid, int(math.sqrt(len(grid))), int(math.sqrt(len(grid[0])))))
                grid = []
            else:
                row = [int(x) for x in line[:-1].split()]
                grid.append(row)
        
        with open(output_file, 'w') as f:
            f.write("Running test script for coursework 1\n")
            f.write("====================================\n")
            for (i, (grid, n_rows, n_cols)) in enumerate(grids):
                grid_origin = copy.deepcopy(grid)
                f.write("Solving grid: %d\n" % (i + 1))
                start_time = time.time()
                solution, steps = solve(grid, n_rows, n_cols)
                elapsed_time = time.time() - start_time
                f.write("Solved in: %f seconds\n" % elapsed_time)
                profile_key = str((min(n_rows, n_cols), max(n_rows, n_cols)))
                if profile_key in profile_time:
                    profile_time[profile_key].append(elapsed_time)
                else:
                    profile_time[profile_key] = [elapsed_time]
                f.write("*** solution ***\n")
                if hint:
                    writelist(get_solution_hint(grid_origin, steps, hint), f)
                else:
                    writelist(solution, f)
                    f.write('\n')
                if is_explain:
                    step_count = min(len(steps), hint) if hint else len(steps)
                    f.write("*** steps ***\n")
                    for step_idx in range(step_count):
                        step = steps[step_idx]
                        f.write("Put {step[2]} in location ({step[0]}, {step[1]})\n")
                if check_solution(solution, n_rows, n_cols):
                    f.write("grid %d correct\n" % (i + 1))
                    points = points + 10
                else:
                    f.write("grid %d incorrect\n" % (i + 1))
            if is_profile:
                for key, value in profile_time.items():
                    profile_time[key] = sum(value) / len(value)
                plt.bar(list(profile_time.keys()), profile_time.values(), width=0.3)
                plt.xlabel("Grid size")
                plt.ylabel("Average time (s)")
                plt.title("Average time taken to solve grids of different sizes")
                plt.show()
        

            f.write("====================================\n")
            f.write("Test script complete, Total points: %d\n" % points)

if __name__ == "__main__":
    main()