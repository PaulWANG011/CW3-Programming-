import task_one_solution_with_12grids as t

#task2.1
def explain():
    f=open(r'output2.1.txt','w')
    for (i, (grid, n_rows, n_cols)) in enumerate(t.grids):
        e=[]#empty space
        #print("Solving grid: %d" % (i + 1))
        f.write("Solving grid: %d" % (i + 1)+ '\n')
        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(row)):
                if grid[i][j] == 0: 
                    e.append((i, j))
        #print(e)            
        sol=t.solve(grid, n_rows, n_cols)
        #print(sol)
        for (i, j) in e:
            f.write(f'Put {sol[i][j]} in location ({i+1},{j+1})'+'\n')
        
    f.close()
    
        
#task 2.2
def file_INPUT_OUTPUT():
    with open (r'output2.2.txt','w') as f:
        for (i, (grid, n_rows, n_cols)) in enumerate(t.grids):
            solution = t.solve(grid, n_rows, n_cols)
            f.write("Solving grid: %d" % (i + 1)+ '\n')
            for line in solution:
                f.write(str(line) + '\n')
                
            

    
def main():
    explain()
    file_INPUT_OUTPUT()
    
if __name__ == "__main__":
    main()
    




