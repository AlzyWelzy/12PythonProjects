# Minesweeper

This is a Python implementation of the classic Minesweeper game. It includes a `Board` class that represents a single game of Minesweeper, and allows for actions such as creating a new game, digging at a location on the board, and rendering the current state of the game.

## Usage

To use the `Board` class, import it from this module and create a new instance with the desired dimensions and number of bombs:

```python
from minesweeper import Board

board = Board(dim_size=8, num_bombs=10)
```

You can then dig at a specific location on the board by calling the dig method and passing it the row and column indices:

```python
board.dig(0, 0)
```
