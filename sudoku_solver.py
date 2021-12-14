from sudoku_lib import ImportSudokuData, PrintSudokuInfo, SudokuSolveZ3;



gridSize, grid = ImportSudokuData("sudoku_data.txt")

PrintSudokuInfo(gridSize, grid)

SudokuSolveZ3(gridSize, grid)