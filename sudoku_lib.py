from typing import List
import math
from z3 import *

GRID_SIZE = [4, 9, 16, 25]

def __CheckGridSize(gridSize: int):
    if(gridSize not in GRID_SIZE):
        raise ValueError('grid size not accepted')

def __CheckGridValue(gridSize: int, val: int):
    if(val < 1 or val > gridSize):
        raise ValueError('grid value not accepted')


def ImportSudokuData(filePath: str):
    f = open(filePath, "r")
    gridSize = int(f.readline())
    __CheckGridSize(gridSize)
    grid = [ [ 0 for j in range(gridSize) ] for i in range(gridSize) ]
    for i in range(gridSize):
        row = f.readline().split(" ")
        for j in range(gridSize):
            col = row[j]
            if(col.isdigit()):
                val = int(col)
                __CheckGridValue(gridSize, val)
                grid[i][j] = val


    f.close()
    return gridSize, grid

def PrintSudokuInfo(gridSize: int, grid: List[List[int]]):
    __CheckGridSize(gridSize)
    subGridSize = int(math.sqrt(gridSize))
    for i in range(gridSize):
        for j in range(gridSize):
            val = grid[i][j] if grid[i][j] > 0 else "-"
            print(val, end= " " if (j+1)%subGridSize else "  ")
        print(end= "\n" if (i+1)%subGridSize else "\n\n")

def SudokuSolveZ3(gridSize: int, grid: List[List[int]]):
    __CheckGridSize(gridSize)
    subGridSize = int(math.sqrt(gridSize))

    #MY VARIABLES
    # 9x9 matrix of integer variables
    X = [ [ Int(f"x_{i+1}_{j+1}") for j in range(gridSize) ] for i in range(gridSize) ]

    #CONSTRAINTS
    # each cell contains a value in {1, ..., gridSize}
    cells_c = [ And(1 <= X[i][j], X[i][j] <= gridSize) for i in range(gridSize) for j in range(gridSize) ]
    # each row contains a digit at most once
    rows_c = [ Distinct(X[i]) for i in range(gridSize) ] #distinct of rows (arrays)
    # each column contains a digit at most once
    cols_c = [ Distinct([ X[i][j] for i in range(gridSize) ]) for j in range(gridSize) ] #distinct of columns (I create the arrays)
    # each subGridSizexsubGridSize square contains a digit at most once
    sq_c = [ Distinct([ X[subGridSize*i0 + i][subGridSize*j0 + j] for i in range(subGridSize) for j in range(subGridSize) ]) for i0 in range(subGridSize) for j0 in range(subGridSize) ]
    # sudoku constraints
    sudoku_c = cells_c + rows_c + cols_c + sq_c
    # instance constraints
    instance_c = [ If(grid[i][j] == 0, True, X[i][j] == grid[i][j]) for i in range(gridSize) for j in range(gridSize) ]
    
    #SOLVER
    s = Solver()
    s.add(sudoku_c + instance_c)
    if s.check() == sat: #s.check() returns "sat" if the solver found a solution
        m = s.model() #returns the solution
        r = [ [ m.evaluate(X[i][j]) for j in range(gridSize) ] for i in range(gridSize) ]
        print_matrix(r)
    else:
        print("failed to solve")