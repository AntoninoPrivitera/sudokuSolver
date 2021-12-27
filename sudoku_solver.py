from sudoku_lib import Difficulty, ImportSudokuData, PrintSudokuInfo, SudokuSolveZ3, SudokuSolveBacktracking, GenerateSudoku;

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
                print("Error in the input to select the solver")
        except Exception as e:
            print(e)
    elif value == "2":
        print("You selected 2 to generate a sudoku")
        print("Difficulties:")
        print("1 - EASY")
        print("2 - MEDIUM")
        print("3 - HARD")
        input_difficulty = input("Please select your difficulty: ")
        try:
            difficulty = int(input_difficulty)
            if difficulty < 1 or difficulty > 3:
                print("Error in the input to select the difficulty")
            else:
                print("Grid size available:")
                print("4 - 4x4")
                print("9 - 9x9")
                print("16 - 16x16")
                print("25 - 25x25")
                input_gridSize = input("Choose the grid size:")
                GenerateSudoku(int(input_gridSize), Difficulty(difficulty))
        except Exception as e:
            print(e)

            
    elif value == "3":
        print("You selected 3 to exit")
        break
    else:
        print("Error in the input to select the command")