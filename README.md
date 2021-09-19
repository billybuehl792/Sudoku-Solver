# Sudoku Solver
Solve sudoku puzzles with backtracking.

## Solve a Puzzle
Pass an array with 0s as unknowns.

```
import Sudoku

puzz_0 = [
    0,0,0,0,0,7,0,3,4,
    0,3,0,0,0,0,0,0,6,
    0,0,4,6,0,8,0,0,0,
    0,9,0,0,1,0,5,0,0,
    0,0,5,2,0,6,3,0,0,
    0,0,2,0,4,0,0,7,0,
    0,0,0,8,0,9,1,0,0,
    9,0,0,0,0,0,0,5,0,
    6,8,0,3,0,0,0,0,0,
]

puzz = Sudoku(puzz_0)
print(puzz.puzzle(solved=True))
```
output:
```
 8  5  6  1  9  7  2  3  4 
 1  3  9  5  2  4  7  8  6 
 2  7  4  6  3  8  9  1  5 
 4  9  8  7  1  3  5  6  2 
 7  1  5  2  8  6  3  4  9 
 3  6  2  9  4  5  8  7  1 
 5  4  7  8  6  9  1  2  3 
 9  2  3  4  7  1  6  5  8 
 6  8  1  3  5  2  4  9  7 
 ```