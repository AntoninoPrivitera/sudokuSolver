from typing import List
import math
from z3 import * #install it through the command: pip install z3-solver
import time

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
        row = f.readline().rstrip('\n').split(" ")
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
    start_time = time.time()

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

    print("--- computation time: %s seconds ---" % (time.time() - start_time))


def SudokuSolveBacktracking(gridSize: int, grid: List[List[int]]):
    start_time = time.time()

    __CheckGridSize(gridSize)
    subGridSize = int(math.sqrt(gridSize))

    result = SudokuSolveBacktrackingRecursive(gridSize, grid, 0 , 0)
    if result:
        PrintSudokuInfo(gridSize, grid)
    else:
        print("impossible to find a solution!")

    print("--- computation time: %s seconds ---" % (time.time() - start_time))


def SudokuSolveBacktrackingRecursive(gridSize: int, grid: List[List[int]], x: int, y: int):
    i = x
    j = y
    while i < gridSize:
        while j < gridSize:
            if(grid[i][j] == 0):
                for val in range(1, gridSize+1):
                    if __checkSudokuConditionBacktracking(gridSize, grid, i, j, val):
                        grid[i][j] = val
                        next_i = i if j < gridSize - 1 else i+1
                        next_j = (j+1)%gridSize
                        result = SudokuSolveBacktrackingRecursive(gridSize, grid, next_i, next_j)
                        if result:
                            return True
                grid[i][j] = 0
                return False
            j += 1
        i += 1
        j = 0
    
    return True


def __checkSudokuConditionBacktracking(gridSize: int, grid: List[List[int]], x, y, val):
    subGridSize = int(math.sqrt(gridSize))

    #check row rule
    for i in range(0, gridSize):
        if grid[i][y] == val:
            return False

    #check column rule
    for j in range(0, gridSize):
        if grid[x][j] == val:
            return False
    
    #check subgrid rule
    firstRow = math.floor(x/subGridSize) * subGridSize
    firstCol = math.floor(y/subGridSize) * subGridSize
    for i in range(firstRow, firstRow + subGridSize):
        for j in range(firstCol, firstCol + subGridSize):
            if grid[i][j] == val:
                return False

    return True