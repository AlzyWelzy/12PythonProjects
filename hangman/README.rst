Hangman
=======

A text-based implementation of the word guessing game, Hangman.

How to Play
-----------

1. Run the script and select a difficulty level:

   -  Easy: 10 incorrect guesses allowed
   -  Medium: 8 incorrect guesses allowed
   -  Hard: 6 incorrect guesses allowed

2. The game will display a word with blank spaces, representing the
   letters that have not yet been guessed.
3. Guess a letter by entering it into the prompt.
4. If the letter is in the word, it will be revealed in the word
   display. If it is not, it will be added to the list of incorrect
   guesses and the hangman ASCII art will be updated to reflect the
   player’s progress.
5. The game will continue until either the player has correctly guessed
   all of the letters in the word, or the player has used up all of
   their allowed incorrect guesses.
6. If the player wins, they will be prompted to play again. If they
   lose, they will also be prompted to play again.

Requirements
------------

-  Python 3
-  JSON module
-  Random module
-  Time module

Customization
-------------

To add or remove words from the game, edit the ``data.json`` file. The
file should contain a JSON object with a single key, ``data``, and the
value should be a list of strings representing the words to be used in
the game.
