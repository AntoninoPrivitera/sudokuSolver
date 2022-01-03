# Sudoku solver and generator
## Tasks
1) The main assignment is to build a Sudoku solver.

The solver should be able to take as input a file containing

n
XXX XXX XXX
XXX XXX XXX
XXX XXX XXX
XXX XXX XXX
XXX XXX XXX
XXX XXX XXX
XXX XXX XXX
XXX XXX XXX
XXX XXX XXX

where n is the size of the grid (e.g. 9 for a n x n grid; n must be 4, 9, 16, 25).
Ignore whitespace and blank lines.
X should be _ or - or . for a square without value given initially, or a hexadecimal digit 0123456789ABCDEFG… (up to 25 digits) (or lowercase).

The solver reduces the problem to SAT. You may use either an external solver (through e.g. DIMACS format) or a solver through a library API (e.g. Z3 API in Python).

This is the main assignment, because that's what you should be ready to do in practice: take a real-world problem, map it to SAT/SMT, solve it.
This is really not difficult.

2) Possible extensions

2 a) Write your own solving algorithm through backtracking. Use some good heuristic to pick the next variable to assign.

2 b) Write a tool for generating Sudoku problems. There are three issues there:
- number of squares given
- unicity of solution
- hardness (which seems to be the amount of backtracking needed for solving).

## Sources
- Project description
  - [Project description](report.pdf)