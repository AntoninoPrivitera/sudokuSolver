from sudoku_lib import ImportSudokuData, PrintSudokuInfo, SudokuSolveZ3, SudokuSolveBacktracking;


#create terminal
value = input("Please enter a string: ")
print(f'You entered {value}')

gridSize, grid = ImportSudokuData("sudoku_data.txt")

print("your file contains the following sudoku to solve:")
PrintSudokuInfo(gridSize, grid)

SudokuSolveZ3(gridSize, grid)

SudokuSolveBacktracking(gridSize, grid)