# Nancy Marino
# CIS256 Fall 2026
# Programming Assignment 4

import pytest
import guess_the_word

def test_choose_word():
    # check selected word is one of the words in the game list
    word = guess_the_word.choose_word()

    assert word in guess_the_word.word_list

def test_correct_guess():
    # Check that a letter found in the word is recognized as correct
    guessed_letters = set()

    result = guess_the_word.process_guess("p", "python", guessed_letters)

    assert result == True
    assert "p" in guessed_letters

def test_incorrect_guess():
    # Check that a letter not found in the word is recognized as incorrect
    guessed_letters = set()

    result = guess_the_word.process_guess("z", "python", guessed_letters)

    assert result == False
    assert "z" in guessed_letters

def test_repeated_letters():
    # check all matching letters appear when a correct letter is guessed
    guessed_letters = {"p"}

    result = guess_the_word.display_word("pepper", guessed_letters)

    assert result == "p_pp__"
