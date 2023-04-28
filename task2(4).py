#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 16:49:00 2023

@author: yux28
"""

import task_one_solution_with_12grids as t
import numpy as np
import matplotlib.pyplot as plt

def profile():
    alle=[]
    for (i, (grid, n_rows, n_cols)) in enumerate(t.grids):
        e=[]
        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(row)):
                if grid[i][j] == 0: 
                    e.append((i, j))
        alle.append(e)
    #print(alle)


    x=[]   #time
    y1=[]  #size
    y2=[]  #number of empty
    for (i, (grid, n_rows, n_cols)) in enumerate(t.grids):
        start_time = t.time.time()
        t.solve(grid, n_rows, n_cols)
        elapsed_time = t.time.time() - start_time
        x.append(elapsed_time)
        y1.append(n_rows*n_cols)
        y2.append(len(alle[i]))#e包含所有grid的空的话

    x=np.array(x)
    y1=np.array(y1)
    y2=np.array(y2)
    plt.bar(x, y1, color='g',width=0.003, label='size of grids')
    plt.bar(x+0.003, y2, color='y', width=0.003, label='number of empty location')
    plt.xlabel('performance in time')
    plt.legend()
    plt.show()
    print(x, y1, y2)
    
def main():
    
    profile()
    
if __name__ == "__main__":
    main()
    