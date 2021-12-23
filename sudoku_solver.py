from sudoku_lib import ImportSudokuData, PrintSudokuInfo, SudokuSolveZ3, SudokuSolveBacktracking;

while True:
    print("COMMANDS:")
    print("1 - solve a sudoku from a file")
    print("2 - generate a sudoku")
    print("3 - exit")
    value = input("Please enter a number to run the command: ")
    match value:
        case "1":
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
                    print("Error in the input to select the solver")
            except Exception as e:
                print(e)
        case "2":
            print("You selected 2 to generate a sudoku")
        case "3":
            print("You selected 3 to exit")
            break
        case _:
            print("Error in the input to select the command")