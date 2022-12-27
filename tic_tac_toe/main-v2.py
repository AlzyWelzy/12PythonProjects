from typing import List, Tuple


class Game:
    def __init__(self):
        self.board = [["-" for i in range(3)] for j in range(3)]
        self.player1_name = None
        self.player2_name = None
        self.player1_symbol = None
        self.player2_symbol = None
        self.current_player = None

    def draw_board(self):
        print("Current board:")
        for row in self.board:
            print(" ".join(row))

    def get_move(self, player: str) -> Tuple[int, int]:
        print(f"\nPlayer {player}'s turn")
        row, col = None, None
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                if row in [0, 1, 2] and col in [0, 1, 2]:
                    if self.board[row][col] == "-":
                        return row, col
                    else:
                        print("That space is already occupied. Try again.")
                else:
                    print("Invalid input. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

    def has_won(self, player: str) -> bool:
        # check rows
        for row in self.board:
            if row == [player, player, player]:
                return True
        # check columns
        for col in range(3):
            if self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player:
                return True
        # check diagonals
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        return False

    def check_draw(self) -> bool:
        for row in self.board:
            if "-" in row:
                return False
        return True

    def main(self):
        while True:
            self.player1_name = input("Player 1, enter your name: ")
            self.player2_name = input("Player 2, enter your name: ")
            print(f"\nWelcome to Tic-Tac-Toe, {self.player1_name} and {self.player2_name}!\n")
            self.player1_symbol = input(f"{self.player1_name}, choose your symbol (X or O): ").upper()
            if self.player1_symbol == "X":
                self.player2_symbol = "O"
            else:
                self.player2_symbol = "X"
            self.board = [["-" for i in range(3)] for j in range(3)]
            self.current_player = self.player1_name
            while True:
                self.draw_board()
                row, col = self.get_move(self.current_player)
                if self.current_player == self.player1_name:
                    symbol = self.player1_symbol
                else:
                    symbol = self.player2_symbol
                self.board[row][col] = symbol
                if self.has_won(symbol):
                    self.draw_board()
                    print(f"\n{self.current_player} has won!")
                    break
                if self.check_draw():
                    self.draw_board()
                    print("\nGame is a draw!")
                    break
                if self.current_player == self.player1_name:
                    self.current_player = self.player2_name
                else:
                    self.current_player = self.player1_name
            if not input("\nWould you like to play again? (y/n) ").lower().startswith("y"):
                break


if __name__ == "__main__":
    game = Game()
    game.main()
