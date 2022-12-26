import json
import random
import time


class Hangman:
    def __init__(self, difficulty="easy"):
        with open("data.json") as f:
            self.words = json.loads(f.read()).get("data")
        self.word = random.choice(self.words)
        self.correct_letters = []
        self.incorrect_letters = []
        self.guesses_remaining = 10
        self.word_letters = set(self.word)
        self.difficulty = difficulty
        self.score = 0
        self.start_time = time.time()

    def display_hangman(self):
        """Displays the hangman ASCII art based on the number of incorrect guesses."""
        if self.guesses_remaining == 10:
            # no incorrect guesses yet, just display the frame
            print("""
 _______
 |     |
 |     
 |     
 |     
 |
_|___
""")
        elif self.guesses_remaining == 9:
            # one incorrect guess, add the head
            print("""
 _______
 |     |
 |     O
 |     
 |     
 |
_|___
""")
        elif self.guesses_remaining == 8:
            # two incorrect guesses, add the body
            print("""
 _______
 |     |
 |     O
 |     |
 |     
 |
_|___
""")
        elif self.guesses_remaining == 7:
            # three incorrect guesses, add the left arm
            print("""
 _______
 |     |
 |     O
 |    /|
 |     
 |
_|___
""")
        elif self.guesses_remaining == 6:
            # four incorrect guesses, add the right arm
            print("""
 _______
 |     |
 |     O
 |    /|\\
 |     
 |
_|___
""")
        elif self.guesses_remaining == 5:
            # five incorrect guesses, add the left leg
            print("""
 _______
 |     |
 |     O
 |    /|\\
 |    / 
 |
_|___
""")
        elif self.guesses_remaining == 4:
            # six incorrect guesses, add the right leg
            print("""
 _______
 |     |
 |     O
 |    /|\\
 |    / \\
 |
_|___
""")

    def set_difficulty(self):
        """Sets the difficulty level of the game."""
        while True:
            print("Select a difficulty level:")
            print("(E)asy, (M)edium, or (H)ard")
            difficulty = input("Enter a letter: ").lower()
            if difficulty == "e":
                self.difficulty = "easy"
                self.guesses_remaining = 10
                break
            elif difficulty == "m":
                self.difficulty = "medium"
                self.guesses_remaining = 8
                break
            elif difficulty == "h":
                self.difficulty = "hard"
                self.guesses_remaining = 6
                break
            else:
                print("Invalid input. Please try again.")

    def play_again(self):
        """Prompts the player to play another round."""
        while True:
            play_again = input("Would you like to play again? (Y/N): ").lower()
            if play_again == "y":
                self.__init__(self.difficulty)
                return True
            elif play_again == "n":
                return False
            else:
                print("Invalid input. Please try again.")

    def game(self):
        """Plays a round of hangman."""
        while True:
            while "-" in self.word or " " in self.word:
                self.word = random.choice(self.words)
            self.word_letters = set(self.word)
            print("Word: ", end="")
            for letter in self.word:
                if letter in self.correct_letters:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
            print("\nIncorrect Letters:", " ".join(self.incorrect_letters))
            print("Guesses Remaining:", self.guesses_remaining)
            self.display_hangman()

            guess = input("Enter a letter: ").lower()

            if guess in self.word:
                self.correct_letters.append(guess)
            else:
                self.incorrect_letters.append(guess)
                self.guesses_remaining -= 1

            if all(letter in self.correct_letters for letter in self.word):
                print("You won! The word was", self.word)
                self.score += 1
                if not self.play_again():
                    print("Thanks for playing! Your final score is", self.score)
                    break
            elif self.guesses_remaining == 0:
                print("You lost the word was", self.word)
                if not self.play_again():
                    print("Thanks for playing! Your final score is", self.score)
                    break


if __name__ == "__main__":
    print("Welcome to Hangman!\n")
    user = Hangman()
    user.set_difficulty()
    user.game()
