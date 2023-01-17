Sudoku Solver
=============

This Python module contains a function ``solve_sudoku`` that solves a
Sudoku puzzle using backtracking.

Function signature
------------------

.. code:: python

   def solve_sudoku(puzzle: List[List[int]]) -> bool:
       """
       Solve a Sudoku puzzle using backtracking.

       Args:
       - puzzle: a 9x9 list of lists representing the puzzle. A value of -1 represents an empty cell.

       Returns:
       - True if a solution exists, False otherwise. The puzzle will be modified in-place to be the solution if one exists.
       """

Example
-------

Here is an example of how to use the solve_sudoku function:

.. code:: python

   from pprint import pprint

   example_board = [
       [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
       [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
       [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

       [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
       [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
       [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],

       [1, -1, -1,   -1, -1, -1,   7, -1, -1],
       [-1, -1,
