import numpy
import math

GRID_SIZE = [4, 9, 16, 25]

def __CheckGridSize(gridSize):
    if(gridSize not in GRID_SIZE):
        raise ValueError('grid size not accepted')

def __CheckGridValue(gridSize, val):
    if(val < 1 or val > gridSize):
        raise ValueError('grid value not accepted')

def ImportSudokuData():
    f = open("sudoku_data.txt", "r")
    gridSize = int(f.readline())
    __CheckGridSize(gridSize)
    grid = numpy.zeros((gridSize, gridSize), dtype=int)
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

def PrintSudokuInfo(gridSize, grid):
    __CheckGridSize(gridSize)
    subGridSize = int(math.sqrt(gridSize))
    for i in range(gridSize):
        for j in range(gridSize):
            val = grid[i][j] if grid[i][j] > 0 else "-"
            print(val, end= " " if (j+1)%subGridSize else "  ")
        print(end= "\n" if (i+1)%subGridSize else "\n\n")