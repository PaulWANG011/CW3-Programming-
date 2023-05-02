def check_solution(grid):
    for i in range(len(grid)):  # this for loop return the fiewset possipility
        ro = grid[i]

        for j in range(len(ro)):
            if type(grid[i][j])==list:
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
                    if i !=0 and type(i)!=list :
                        numbers_list.append(i)  # add the numbers of the square
    for i in grid[which_row]:#collecting numbers in the same row
        if i != 0 and type(i)!=list:
            numbers_list.append(i)  # add the numbers in the row
    for i in range(0, n_cols * n_rows):#collecting numbers in the same colum
        colum_number = grid[i][which_coulm]
        if colum_number!=0 and type(colum_number)!=list:
            numbers_list.append(colum_number)  # add the numbers in the same colum

    all_numbers=[*range(1,n_cols*n_rows+1)]#all numbers that can be added to the soduco
    all_numbers=set(all_numbers)
    possiple_numbers=all_numbers.symmetric_difference(set(numbers_list))#all possiple numbers that can be added to the empety space(0)
    return list(possiple_numbers)


def adding_lists(grid,col,row):
    for i in range(len(grid)):  # this for loop return the fiewset possipility
        ro = grid[i]

        for j in range(len(ro)):
            if grid[i][j] == 0:
                b=the_missing_numbers(grid,col,row,i,j)
                grid[i][j]=b
    return grid

def filling_in(grid):
    listt=[]
    for i in range(len(grid)):
        l=grid[i]
        for j in range(len(grid)):
              if type(grid[i][j])==list :
                  listt.append(len(grid[i][j]))
    for i in range(len(grid)):
        l = grid[i]
        for j in range(len(l)):
             if type(grid[i][j]) == list and len(grid[i][j]) ==min(listt):
                 for n in grid[i][j]:
                    grid[i][j] = n
                    return [grid, i, j, n]


def after_(grid,n_rows,n_cols,whichrow,whichcoulm,n):
    numbers_list = []#list to collect numbers that can not be added to the empty(0)

    for i in range(n_cols):#collecting numbers in the same sequare
        rows = (i * n_rows, (i + 1) * n_rows)
        for j in range(n_rows):
            cols = (j * n_cols, (j + 1) * n_cols)
            square = []
            for k in range(rows[0], rows[1]):
                line = grid[k][cols[0]:cols[1]]
                square += line
            if whichcoulm in range(cols[0], cols[1]) and whichrow in range(rows[0], rows[1]):
                for i in square:
                    if type(i)==list :
                        for mama in i:
                            if mama==n:
                                i.remove(n) # add the numbers of the square
    for i in grid[whichrow]:#collecting numbers in the same row
        if type(i)==list:
            for mama in i:
                if mama==n:
                    i.remove(n)  # add the numbers in the row
    for i in range(0, n_cols * n_rows):#collecting numbers in the same colum
        colum_number = grid[i][whichcoulm]
        if type(colum_number)==list:
            for nona in colum_number:
                if nona == n:
                    colum_number.remove(n)# add the numbers in the same colum
    return grid

def after(grid,n_rows,n_cols):
    h=filling_in(grid)
    hoha = grid
    if h :
        hoha=after_(h[0],n_rows,n_cols,h[1],h[2],h[3])

    return hoha
def solve(grid, n_col,n_row):
    grid=adding_lists(grid,n_col,n_row)
    while not check_solution(grid):
        grid=after(grid,n_row,n_col)
    return grid
