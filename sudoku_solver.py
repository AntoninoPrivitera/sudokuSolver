from sudoku_lib import ImportSudokuData, PrintSudokuInfo, PrintSudokuInfoFile, SudokuSolveZ3, SudokuSolveBacktracking, GenerateSudoku;

while True:
    print("COMMANDS:")
    print("1 - solve a sudoku from a file")
    print("2 - generate a sudoku")
    print("3 - exit")
    value = input("Please enter a number to run the command: ")
    if value == "1":
        print("You selected 1 to solve a sudoku from a file")
        filename = input("Please add the file name which contains your sudoku (empty if you want to use sudoku_data.txt as default): ")
        
        try:
            gridSize, grid = ImportSudokuData("sudoku_data.txt" if filename == "" else filename)

            print("your file contains the following sudoku to solve:")
            PrintSudokuInfo(gridSize, grid)

            solver = input("Which solver do you want to use? (1 - z3, 2 - backtracking): ")
            if solver == "1":
                SudokuSolveZ3(gridSize, grid)
            elif solver == "2":
                SudokuSolveBacktracking(gridSize, grid)
            else:
                raise ValueError("Error in the input to select the solver")
        except Exception as e:
            print(e)
    elif value == "2":
        print("You selected 2 to generate a sudoku")
        try:            
            print("Choose a solver to fill your sudoku")
            inputFillerType = input("Do you want to use z3 (1) or backtracking (2)? ")
            if inputFillerType != "1" and inputFillerType != "2":
                raise ValueError('Error in the input to select solver as filler')

            print("Grid size available:")
            print("4 - 4x4")
            print("9 - 9x9")
            print("16 - 16x16")
            print("25 - 25x25")
            gridSize = int(input("Choose the grid size:"))
            gridsCellsRemoved = GenerateSudoku(gridSize, True if inputFillerType == "1" else False)
            numberOfCellsRemovedMax = len(gridsCellsRemoved)
            print(f"Number of cells removed are {numberOfCellsRemovedMax} after 5 attempts.")
            inputCellsChosen = int(input(f"How many cells do you want to remove between {1} and {numberOfCellsRemovedMax}? "))
            if inputCellsChosen < 1 or inputCellsChosen > numberOfCellsRemovedMax:
                raise ValueError('Error in the input to select the number of cells to remove')
            
            gridChosen = gridsCellsRemoved[inputCellsChosen-1]
            print("Your final sudoku is:")
            PrintSudokuInfo(gridSize, gridChosen)
            print("Your final sudoku in file format is:")
            PrintSudokuInfoFile(gridSize, gridChosen)
        except Exception as e:
            print(e)

            
    elif value == "3":
        print("You selected 3 to exit")
        break
    else:
        print("Error in the input to select the command")