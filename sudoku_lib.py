from typing import List
import math
from z3 import * #install it through the command: pip install z3-solver

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
    n_digits = len(str(gridSize))
    __CheckGridSize(gridSize)
    subGridSize = int(math.sqrt(gridSize))
    for i in range(gridSize):
        for j in range(gridSize):
            val = str(grid[i][j]).zfill(n_digits) if grid[i][j] > 0 else "-"*n_digits
            print(val, end= " " if (j+1)%subGridSize else "  ")
        print(end= "\n" if (i+1)%subGridSize else "\n\n")

def SudokuSolveZ3(gridSize: int, grid: List[List[int]]):
    __CheckGridSize(gridSize)
    subGridSize = int(math.sqrt(gridSize))

    #MY VARIABLES
    X = [ [ Int(f"x_{i+1}_{j+1}") for j in range(gridSize) ] for i in range(gridSize) ] # my matrix is composed by gridSize*gridSize variables

    #CONSTRAINTS
    cells = [ And(1 <= X[i][j], X[i][j] <= gridSize) for i in range(gridSize) for j in range(gridSize) ] # each cell has a value  between 1 and gridSize
    rows = [ Distinct(X[i]) for i in range(gridSize) ] # each number is unique for each row
    columns = [ Distinct([ X[i][j] for i in range(gridSize) ]) for j in range(gridSize) ] # each number is unique for each column
    
    submatrix = [ Distinct([ X[subGridSize*i0 + i][subGridSize*j0 + j] for i in range(subGridSize) for j in range(subGridSize) ]) for i0 in range(subGridSize) for j0 in range(subGridSize) ] # each submatrix subGridSizexsubGridSize has each number unique
    instance = [ If(grid[i][j] == 0, True, X[i][j] == grid[i][j]) for i in range(gridSize) for j in range(gridSize) ] # problem instance constraints
    sudoku = cells + rows + columns + submatrix + instance # sudoku constraints

    #SOLVER
    s = Solver()
    s.add(sudoku)
    if s.check() == sat: #s.check() returns "sat" if the solver found a solution
        m = s.model() #returns the solution
        print("your solution is:")
        gridSolution = [ [ m[X[i][j]].as_long() for j in range(gridSize) ] for i in range(gridSize) ]  # as_long() allows to get the value as int type
        PrintSudokuInfo(gridSize, gridSolution)
    else:
        print("impossible to find a solution!")


def SudokuSolveBacktracking(gridSize: int, grid: List[List[int]]):
    __CheckGridSize(gridSize)
    subGridSize = int(math.sqrt(gridSize))
    print("impossible to find a solution!")