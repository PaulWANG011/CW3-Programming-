import random
import copy
import time

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
grid7_easy=[[9, 0, 6, 0, 0, 1, 0, 4, 0],
[7, 0, 1, 2, 9, 0, 0, 6, 0],
[4, 0, 2, 8, 0, 6, 3, 0, 0],
[0, 0, 0, 0, 2, 0, 9, 8, 0],
[6, 0, 0, 0, 0, 0, 0, 0, 2],
[0, 9, 4, 0, 8, 0, 0, 0, 0],
[0, 0, 3, 7, 0, 8, 4, 0, 9],
[0, 4, 0, 0, 1, 3, 7, 0, 6],
[0, 6, 0, 9, 0, 0, 1, 0, 8]]
grid8_easy=[[0, 0, 0, 2, 6, 0, 7, 0, 1],
[6, 8, 0, 0, 7, 0, 0, 9, 0],
[1, 9, 0, 0, 0, 4, 5, 0, 0],
[8, 2, 0, 1, 0, 0, 0, 4, 0],
[0, 0, 4, 6, 0, 2, 9, 0, 0],
[0, 5, 0, 0, 0, 3, 0, 2, 8],
[0, 0, 9, 3, 0, 0, 0, 7, 4],
[0, 4, 0, 0, 5, 0, 0, 3, 6],
[7, 0, 3, 0, 1, 8, 0, 0, 0]]
grid9_easy=[[0, 3, 0, 4, 0, 0],
[0, 0, 5, 6, 0, 3],
[0, 0, 0, 1, 0, 0],
[0, 1, 0, 3, 0, 5],
[0, 6, 4, 0, 3, 1],
[0, 0, 1, 0, 4, 6]]
grid10_mid=[[0, 0, 0, 6, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 5, 0, 1],
[3, 6, 9, 0, 8, 0, 4, 0, 0],
[0, 0, 0, 0, 0, 6, 8, 0, 0],
[0, 0, 0, 1, 3, 0, 0, 0, 9],
[4, 0, 5, 0, 0, 9, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 3, 0, 0],
[0, 0, 6, 0, 0, 7, 0, 0, 0],
[1, 0, 0, 3, 4, 0, 0, 0, 0]]
grid11_mid=[[8, 0, 9, 0, 2, 0, 3, 0, 0],
[0, 3, 7, 0, 6, 0, 5, 0, 0],
[0, 0, 0, 4, 0, 9, 7, 0, 0],
[0, 0, 2, 9, 0, 1, 0, 6, 0],
[1, 0, 0, 3, 0, 6, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 3],
[7, 0, 0, 0, 0, 0, 0, 0, 8],
[5, 0, 0, 0, 0, 0, 0, 1, 4],
[0, 0, 0, 2, 8, 4, 6, 0, 5]]
grid12_hard=[[0, 2, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 6, 0, 4, 0, 0, 0, 0],
[5, 8, 0, 0, 9, 0, 0, 0, 3],
[0, 0, 0, 0, 0, 3, 0, 0, 4],
[4, 1, 0, 0, 8, 0, 6, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 9, 5],
[2, 0, 0, 0, 1, 0, 0, 8, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 3, 1, 0, 0, 8, 0, 5, 7]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2), (grid6, 2, 3),(grid7_easy, 3, 3),(grid8_easy,3,3),(grid9_easy,2,3),(grid10_mid,3,3),(grid11_mid,3,3),(grid12_hard,3,3)]
'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''


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


def the_missing_numbers(grid, n_cols, n_rows, which_row, which_coulm):
    '''the arguemnts are grid=the grid we need to solve,
    n_cols and n_rows=the number of colums and rows in each sequare in the grid,
     which_reow and which_coulm= the colum and row the 0 in(location of 0),
    this function will be called in find empty function to select the empty location with the fewest number of variable options to fill'''
    numbers_list = []#list to collect numbers that can not be added to the empty(0)
    for i in range(n_cols):#collecting numbers in the same sequare
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
    for i in grid[which_row]:#collecting numbers in the same row
        if i != 0:
            numbers_list.append(i)  # add the numbers in the row
    for i in range(0, n_cols * n_rows):#collecting numbers in the same colum
        colum_number = grid[i][which_coulm]
        if colum_number!=0:
            numbers_list.append(colum_number)  # add the numbers in the same colum
    numbers_list=set(numbers_list)
    all_numbers=[*range(1,n_cols*n_rows+1)]#all numbers that can be added to the soduco
    all_numbers=set(all_numbers)
    possiple_numbers=all_numbers.symmetric_difference(numbers_list)#all possiple numbers that can be added to the empety space(0)
    return list(possiple_numbers)

def find_empty(grid, n_col, n_row):
    '''
	This function returns the index (i, j) to the feweist posibilities zero element in a sudoku grid
	If no such element is found, it returns None

	args: grid
	return: A tuple (i,j) where i and j are both integers, or None
	'''
    list=[]
    for i in range(len(grid)):#this for loop collect the amout of possile numbers for every empty(0)
        row = grid[i]

        for j in range(len(row)):
            if grid[i][j] == 0:
                b=len(the_missing_numbers(grid,n_col,n_row,i,j))
                list.append(b)

    for i in range(len(grid)):#this for loop return the fiewset possipility
        row = grid[i]

        for j in range(len(row)):
            if grid[i][j] == 0:
                if len(the_missing_numbers(grid, n_col, n_row, i, j)) == min(list):
                    return (i, j)
    for n in range(len(grid)):#this for loop help increasing the velocity of the code
        row = grid[i]

        for m in range(len(row)):
            if grid[i][j] == 0:
                return (i, j)
    return None


def recursive_solve(grid, n_rows, n_cols):
    '''
	This function uses recursion to exhaustively search all possible solutions to a grid
	until the solution is found

	args: grid, n_rows, n_cols
	return: A solved grid (as a nested list), or None
	'''

    # N is the maximum integer considered in this board
    n = n_rows * n_cols
    # Find an empty place in the grid
    empty = find_empty(grid, n_cols, n_rows)

    # If there's no empty places left, check if we've found a solution
    if not empty:
        # If the solution is correct, return it.
        if check_solution(grid, n_rows, n_cols):
            return grid
        else:
            # If the solution is incorrect, return None
            return None
    else:
        row, col = empty

    # Loop through possible values
    for i in range(1, n + 1):
        if i in the_missing_numbers(grid,n_cols,n_rows,row,col):#add to increase the velocity
        # Place the value into the grid
            grid[row][col] = i
        # Recursively solve the grid
            ans = recursive_solve(grid, n_rows, n_cols)
        # If we've found a solution, return it
            if ans:
                return ans

        # If we couldn't find a solution, that must mean this value is incorrect.
        # Reset the grid for the next iteration of the loop
        grid[row][col] = 0

    # If we get here, we've tried all possible values. Return none to indicate the previous value is incorrect.
    return None


def random_solve(grid, n_rows, n_cols, max_tries=50000):
    '''
	This function uses random trial and error to solve a Sudoku grid

	args: grid, n_rows, n_cols, max_tries
	return: A solved grid (as a nested list), or the original grid if no solution is found
	'''

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
    '''
	Solve function for Sudoku coursework.
	Comment out one of the lines below to either use the random or recursive solver
	'''

    #return random_solve(grid, n_rows, n_cols)
    return recursive_solve(grid, n_rows, n_cols)


'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''


def main():
    points = 0

    print("Running test script for coursework 1")
    print("====================================")

    for (i, (grid, n_rows, n_cols)) in enumerate(grids):
        print("Solving grid: %d" % (i + 1))
        start_time = time.time()
        solution = solve(grid, n_rows, n_cols)
        elapsed_time = time.time() - start_time
        print("Solved in: %f seconds" % elapsed_time)
        print(solution)
        if check_solution(solution, n_rows, n_cols):
            print("grid %d correct" % (i + 1))
            points = points + 10
        else:
            print("grid %d incorrect" % (i + 1))

    print("====================================")
    print("Test script complete, Total points: %d" % points)


if __name__ == "__main__":
    main()
