# Sudoku Solver

This Python module contains a function `solve_sudoku` that solves a Sudoku puzzle using backtracking.

## Function signature

```python
def solve_sudoku(puzzle: List[List[int]]) -> bool:
    """
    Solve a Sudoku puzzle using backtracking.

    Args:
    - puzzle: a 9x9 list of lists representing the puzzle. A value of -1 represents an empty cell.

    Returns:
    - True if a solution exists, False otherwise. The puzzle will be modified in-place to be the solution if one exists.
    """
```
