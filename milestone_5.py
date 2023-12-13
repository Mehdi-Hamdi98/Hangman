import random
from collections import Counter


class Hangman:
    def __init__(self, word_list, num_lives=5) -> None:
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(
            [letter for letter in set(self.word) if letter not in self.word_guessed]
        )
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for index, letter in enumerate(self.word_guessed, start=0):
                if letter == "_" and self.word[index] == guess:
                    self.word_guessed.pop(index)
                    self.word_guessed.insert(index, guess)
                    break
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        guess = input("Enter a single letter guess: ")

        if len(guess) != 1 and not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif (
            guess in self.list_of_guesses
            and Counter(self.word)[guess] == Counter(self.list_of_guesses)[guess]
        ):
            print("You already tried that letter!")
        else:
            self.list_of_guesses.append(guess)
            self.check_guess(guess)


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives <= 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives > 0 and game.num_letters <= 0:
            print("Congratulations. You won the game!")


play_game(["apple", "banana", "orange", "grapes", "mango"])
