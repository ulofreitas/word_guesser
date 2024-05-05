"""
File: word_guess.py
-------------------
"""

import random

LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with

def play_game(secret_word):
    """
    Add your code
    """
    print("Welcome to the game, guess the word!!")
    guess = input("Type a single letter here, then press enter: ").upper()
    pass


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.
    """
    ALL_WORDS = []
    # Go through the file of all words (Lexicon.txt), process each line,
    # and add it to a list of all words.
    file = open("Lexicon.txt", "r")
    for line in file:
        ALL_WORDS.append(line.rstrip("\n"))
    print(f"These are all the words we can choose from {ALL_WORDS}")  # delete, this is to show all the words!
    # TODO: Randomly select a word from the options
    return ALL_WORDS[0]  # Placeholder, replace with the TODO item


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()