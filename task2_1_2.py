# -*- coding: utf-8 -*-
# coding=utf-8
import task_one_solution_with_12grids as t  #in order to use task1's function in more concise way
import sys                                  #in order to use flag
args=len(sys.argv)

'''task2.1'''
def explain():
    f=open(r'output2.1.txt','w')
    for (i, (grid, n_rows, n_cols)) in enumerate(t.grids):
        e=[]
        f.write("Solving grid: %d" % (i + 1)+ '\n')
        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(row)):
                if grid[i][j] == 0: 
                    e.append((i, j))
                   
        sol=t.solve(grid, n_rows, n_cols)
        
        for (i, j) in e:
            f.write(f'Put {sol[i][j]} in location ({i+1},{j+1})'+'\n') #write what we want in output2.1.txt
        
    f.close()
    
        
'''task 2.2'''
def file_INPUT_OUTPUT():
    with open (r'output2.2.txt','w') as f:
        for (i, (grid, n_rows, n_cols)) in enumerate(t.grids):
            solution = t.solve(grid, n_rows, n_cols)
            f.write("Solving grid: %d" % (i + 1)+ '\n')
            for line in solution:
                f.write(str(line) + '\n')
                
            

    
def main(args):
    
    one = args[0]   #we set the args in cmd: task2_1_2.py one

    if one =='--explain':               #flag --explain
        explain()
        
    if one =='--file_INPUT_OUTPUT':     #flag --file_INPUT_OUTPUT
        file_INPUT_OUTPUT()
        
        

    
if __name__ == "__main__":
    main(sys.argv[1:]) #let it run except the file name
    
    
    




