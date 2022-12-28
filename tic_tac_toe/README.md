# Tic-Tac-Toe AI

This code includes four classes for playing Tic-Tac-Toe:

- `Player`: An abstract class representing a player in the game.
- `HumanPlayer`: A subclass of `Player` that allows a human player to input their move.
- `RandomComputerPlayer`: A subclass of `Player` that chooses a random valid move.
- `SmartComputerPlayer`: A subclass of `Player` that uses the minimax algorithm to choose the best possible move.

## `Player`

The `Player` class has one attribute:

- `letter`: The letter (either 'X' or 'O') representing the player's symbol in the game.

It has one method:

- `get_move(game)`: A method that returns the player's chosen move for the given game. This method should be implemented in subclasses.

## `HumanPlayer`

The `HumanPlayer` class is a subclass of `Player` that allows a human player to input their move. It has no additional attributes or methods.

## `RandomComputerPlayer`

The `RandomComputerPlayer` class is a subclass of `Player` that chooses a random valid move. It has no additional attributes or methods.

## `SmartComputerPlayer`

The `SmartComputerPlayer` class is a subclass of `Player` that uses the minimax algorithm to choose the best possible move. It has one additional method:

- `minimax(state, player)`: A recursive method that uses the minimax algorithm to determine the optimal move for the given player in the given state of the game. It returns a dictionary with the optimal position to move to and the score for that move.
