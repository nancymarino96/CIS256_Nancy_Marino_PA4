# Nancy Marino
# CIS256 Fall 2026
# Programming Assignment 4

import random

# words the game can randomly choose from
word_list = ["python", "computer", "program", "keyboard", "internet"]

def choose_word():
    # select one random word from list
    return random.choice(word_list)

def process_guess(guess, word, guessed_letters):
    # Check the guessed letter is in the word
    guessed_letters.add(guess.lower())

    if guess.lower() in word:
        return True
    else:
        return False

def display_word(word, guessed_letters):
    # Show correct guessed letters and hide the remaining ones
    displayed_word = ""

    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"

    return displayed_word

def play_game():
    # start a new game with a randomly selected word
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Guess the Word")
    print("Guess one letter at a time")

    # keep playing while attempts remain and the word is incomplete
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts remaining:", attempts)

        guess = input("Enter a letter: ").lower().strip()

        # check the player enters exactly one letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter")
            continue

        # dont count the same letter more than once
        if guess in guessed_letters:
            print("You already guessed that letter")
            continue

        if process_guess(guess, word, guessed_letters):
            print("Correct guess!")
        else:
            print("Incorrect guess!")
            attempts -= 1

        # Check every letter in the word has been guessed
        if display_word(word, guessed_letters) == word:
            print("\nCongratulations! You guessed the word!")
            print("The word was:", word)
            return

    print("\nGame over! You ran out of attempts.")
    print("The word was:", word)

# start the game when this file is run.
if __name__ == "__main__":
    play_game()
