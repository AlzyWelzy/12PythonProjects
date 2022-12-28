from typing import List, Tuple


class Game:

    def init(self, player1_name: str, player2_name: str):
        # Initialize game board, player names, and symbols
        self.board = [["-" for i in range(3)] for j in range(3)]
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_symbol = None
        self.player2_symbol = None
        self.current_player = None
        self.player1_score = 0
        self.player2_score = 0
        self.game_history = []

    def draw_board(self):
        # Print current game board
        print("Current board:")
        for row in self.board:
            print(" ".join(row))

    def get_move(self, player: str) -> Tuple[int, int]:
        # Prompt player for row and column and check if the space is available
        print(f"\nPlayer {player}'s turn")
        row, col = None, None
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                if row in [0, 1, 2] and col in [0, 1, 2]:
                    if self.board[row][col] == "-":
                        # Update current player
                        if self.current_player == self.player1_name:
                            self.current_player = self.player2_name
                        else:
                            self.current_player = self.player1_name
                        return row, col
                    else:
                        print("That space is already occupied. Try again.")
                else:
                    print("Invalid input. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

    def has_won(self, player: str) -> bool:
        # Check rows, columns, and diagonals for winning combination
        for row in self.board:
            if row == [player, player, player]:
                return True
        for col in range(3):
            if self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player:
                return True
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        return False

    def check_draw(self) -> bool:
        # Check if the game is a draw
        for row in self.board:
            if "-" in row:
                return False
        return True

    def update_score(self, player: str):
        # Increment player's score by 1
        if player == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def update_history(self, winner: str):
        # Add current game board and winner to game history
        self.game_history.append((self.board, winner))

    def print_history(self):
        # Print game history
        for i, game in enumerate(self.game_history):
            print(f"\nGame {i+1}:")
        for row in game[0]:
            print(" ".join(row))
        print(f"Winner: {game[1]}")

    def play_game(self) -> None:
        # Prompt player 1 for symbol and assign symbol for player 2
        self.player1_symbol = input(
            f"{self.player1_name}, choose your symbol (X or O): ").upper()
        if self.player1_symbol == "X":
            self.player2_symbol = "O"
        else:
            self.player2_symbol = "X"
            self.current_player = self.player1_name

        while True:
            # Draw board and get move for current player
            self.draw_board()
            row, col = self.get_move(self.current_player)
