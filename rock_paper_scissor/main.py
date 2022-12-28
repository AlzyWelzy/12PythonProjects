import random

# The RockPaperScissor class represents a game of rock-paper-scissors


class RockPaperScissor:
    def __init__(self):
        # Initialize the list of options (rock, paper, scissor)
        self.options = ["rock", "paper", "scissor"]

        # Initialize the rules for winning and losing
        self.rules = {
            "rock": "scissor",  # rock beats scissor
            "paper": "rock",  # paper beats rock
            "scissor": "paper"  # scissor beats paper
        }

        # Initialize a dictionary to keep track of the result of each game
        self.result = {"win": 0, "lose": 0, "tie": 0}

    def game(self):
        # Play a single game of rock-paper-scissors
        while True:
            # Prompt the player to choose rock, paper, or scissor
            player_choice = input("Choose rock, paper, or scissor: ")

            # If the player's choice is not valid, prompt them to try again
            if player_choice not in self.options:
                print("Invalid choice, please try again.")
                continue

            # Select a random option for the computer
            computer_choice = random.choice(self.options)
            print(f"The computer chose {computer_choice}.")

            # Compare the player's and computer's choices and update the result dictionary accordingly
            if player_choice == computer_choice:
                self.result["tie"] += 1
                print("It's a tie!")
            elif self.rules[player_choice] == self.rules[computer_choice]:
                self.result["win"] += 1
                print("You win!")
            else:
                self.result["lose"] += 1
                print("You lose!")

            # Ask the player if they want to play again
            player_again = input("Do you want to play again? [y/n].")
            if player_again.lower() != "y":
                # Print the final result of the games played and exit the loop
                print(
                    f"Result is {self.result['win']} : {self.result['lose']} : {self.result['tie']}")
                break


# Create an instance of the RockPaperScissor class and start playing
user = RockPaperScissor()
user.game()
