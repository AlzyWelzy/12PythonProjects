board = [["-" for i in range(3)] for j in range(3)]


def draw_board():
    print("Current board:")
    for row in board:
        print(" ".join(row))


def get_move():
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
    while True:
        print("Welcome to Tic-Tac-Toe!\n")
        player1_symbol = input("Player 1, choose your symbol (X or O): ").upper()
        if player1_symbol == "X":
            player2_symbol = "O"
        else:
            player2_symbol = "X"
        draw_board()
        player = player1_symbol
        while True:
            print(f"\nPlayer {player}'s turn")
            row, col = get_move()
            board[row][col] = player
            draw_board()
            if has_won(player):
                print(f"\nPlayer {player} has won!")
                break
            if check_draw():
                print("\nGame is a draw!")
                break
            if player == player1_symbol:
                player = player2_symbol
            else:
                player = player1_symbol
        if not input("\nWould you like to play again? (y/n) ").lower().startswith("y"):
            break


main()
