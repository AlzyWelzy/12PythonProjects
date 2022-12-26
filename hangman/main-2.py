import json
import random


class Hangman:
    def __init__(self):
        with open("data.json") as f:
            self.words = json.loads(f.read()).get("data")
        self.word = random.choice(self.words)
        self.correct_letters = []
        self.incorrect_letters = []
        self.guess_remaining = 10
        self.word_letters = set(self.word)

    def game(self):
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
            print("Guesses Remaining:", self.guess_remaining)

            guess = input("Enter a letter: ").lower()

            if guess in self.word:
                self.correct_letters.append(guess)
            else:
                self.incorrect_letters.append(guess)
                self.guess_remaining -= 1

            if all(letter in self.correct_letters for letter in self.word):
                print("You won! The word was", self.word)
            elif self.guess_remaining == 0:
                print("You lost the word was", self.word)
                break


user = Hangman()
user.game()
