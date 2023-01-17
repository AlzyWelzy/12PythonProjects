GuessNumber
===========

A simple game where the player or the computer tries to guess a randomly
generated number.

How to Play
-----------

1. Run the script and choose whether you want to be the one guessing or
   have the computer guess.
2. If you choose to be the one guessing, enter a positive integer
   between 1 and 1000000000 into the prompt. The game will tell you if
   your guess is too high or too low.
3. If the computer is guessing, it will generate random guesses until it
   guesses the correct number.
4. The game will keep track of the number of guesses made and display
   the high score when the game is over.

Requirements
------------

-  Python 3
-  Random module

Customization
-------------

To change the range of the randomly generated number, edit the
``randint`` function in the ``guess`` and ``comp_guess`` methods.
