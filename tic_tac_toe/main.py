board = [["-" for i in range(3)] for j in range(3)]


def draw_board():
    print("Current board:")
    for row in board:
        print(" ".join(row))


def get_move(player):
    print(f"\nPlayer {player}'s turn")
    row, col = None, None
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if row in [0, 1, 2] and col in [0, 1, 2]:
                if board[row][col] == "-":
                    return row, col
                else:
                    print("That space is already occupied. Try again.")
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Invalid input. Try again.")


def has_won(player):
    # check rows
    for row in board:
        if row == [player, player, player]:
            return True
    # check columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def check_draw():
    for row in board:
        if "-" in row:
            return False
    return True


def main():
    player1_name = input("Player 1, enter your name: ")
    player2_name = input("Player 2, enter your name: ")
    while True:
        print(f"\nWelcome to Tic-Tac-Toe, {player1_name} and {player2_name}!\n")
        player1_symbol = input(f"{player1_name}, choose your symbol (X or O): ").upper()
        if player1_symbol == "X":
            player2_symbol = "O"
        else:
            player2_symbol = "X"
        draw_board()
        player = player1_name
        while True:
            row, col = get_move(player)
            if player == player1_name:
                symbol = player1_symbol
            else:
                symbol = player2_symbol
            board[row][col] = symbol
            draw_board()
            if has_won(symbol):
                print(f"\n{player} has won!")
                break
            if check_draw():
                print("\nGame is a draw!")
                break
            if player == player1_name:
                player = player2_name
            else:
                player = player1_name
        if not input("\nWould you like to play again? (y/n) ").lower().startswith("y"):
            break


if __name__ == "__main__":
    main()
