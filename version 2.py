
def is_valid(num, row, col, grid):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    subgrid_row = (row // 3) * 3
    subgrid_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[subgrid_row+i][subgrid_col+j] == num:
                return False
    return True

def solve(grid, row=0, col=0):
    if row == 9:
        return True
    next_row = row + (col + 1) // 9
    next_col = (col + 1) % 9
    if grid[row][col] != 0:
        return solve(grid, next_row, next_col)
    for num in range(1, 10):
        if is_valid(num, row, col, grid):
            grid[row][col] = num
            if solve(grid, next_row, next_col):
                return True
            grid[row][col] = 0
    return False

# Prompt the user to input the initial state of the puzzle
grid = []
for i in range(9):
    row = []
    for j in range(9):
        row.append(int(input("Enter value for row %d, column %d: " % (i+1, j+1))))
    grid.append(row)

# Solve the puzzle
if solve(grid):
    for row in grid:
        print(row)
else:
    print("No solution found")

