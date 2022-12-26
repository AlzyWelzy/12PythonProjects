import random


class GuessNumber:
    def __init__(self):
        self.randNum = None
        self.guessNum = 0
        self.guesses = 0

    @staticmethod
    def hiscore(guesses):
        with open("./12Projects/guessNumber/hiscore.txt") as f:
            cur_hi_score = int(f.read())

        if cur_hi_score > guesses:
            with open('./12Projects/guessNumber/hiscore.txt', "w") as f:
                f.write(str(guesses))
                print(
                    f"YOU HAVE SURPASSED YOUR PREVIOUS HIGH SCORE {cur_hi_score}, YOUR NEW HIGH SCORE IS {guesses}.")

    def guess(self):
        self.randNum = random.randint(1, 1000000000)

        while self.randNum != self.guessNum:

            try:
                self.guessNum = int(
                    input("Enter a positive integer between 1 to 1000000000: "))
                if self.randNum == self.guessNum:
                    print(
                        f"You managed to complete the game in {self.guesses}.")
                    self.hiscore(self.guesses)
                else:
                    if self.guessNum > self.randNum:
                        print("Too High")
                        self.guesses += 1
                    elif self.guessNum < self.randNum:
                        print("Too Low")
                        self.guesses += 1

            except Exception as e:
                print(e)

    @staticmethod
    def comp_guess():
        guesses = 0
        try:
            user = int(input("Enter a positive integer between 1 to 1000000000: "))
            comp = 0
            while user != comp:
                comp = random.randint(1, 1000000000)
                if user == comp:
                    print(f"Computer guesses it in {guesses}.")
                else:
                    if comp > user:
                        guesses += 1
                        print("Too High")
                    else:
                        guesses += 1
                        print("Too Low")

        except Exception as e:
            print(e)


newU = GuessNumber()

newU.comp_guess()
