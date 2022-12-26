import random
import tkinter as tk


class Player:
    def __init__(self, name):
        self.name = name
        self.guesses = 0


class Game:
    def __init__(self, player, min_num, max_num):
        self.player = player
        self.min_num = min_num
        self.max_num = max_num
        self.target_num = None
        self.create_ui()
        self.start_game()

    def start_game(self):
        self.target_num = random.randint(self.min_num, self.max_num)
        self.player.guesses = 0

    def guess(self):
        try:
            guess = int(self.input_box.get())
            self.player.guesses += 1
            if guess == self.target_num:
                self.game_over()
            elif guess > self.target_num:
                self.output_label.config(text="Too high!")
            elif guess < self.target_num:
                self.output_label.config(text="Too low!")
        except ValueError:
            self.output_label.config(text="Please enter a valid number!")

    def game_over(self):
        self.output_label.config(
            text=f"You guessed the number in {self.player.guesses} guesses!")
        self.input_box.config(state=tk.DISABLED)
        self.guess_button.config(state=tk.DISABLED)

    def create_ui(self):
        self.root = tk.Tk()
        self.root.title("Guess the Number")

        self.input_box = tk.Entry(self.root)
        self.input_box.pack()

        self.guess_button = tk.Button(
            self.root, text="Guess", command=self.guess)
        self.guess_button.pack()

        self.output_label = tk.Label(self.root, text="")
        self.output_label.pack()


player = Player("Player 1")
game = Game(player, 1, 6)
game.create_ui()
game.root.mainloop()
