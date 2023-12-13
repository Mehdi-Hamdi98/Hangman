import random
import string

word_list = ["banana", "apple", "mango", "orange", "grapes"]
print(word_list)

word = random.choice(word_list)
print(word)


def ask_for_input():
    while True:
        guess = input("Enter a single letter: ")

        if len(guess) == 1 and guess.isalpha():
            print("Good guess!")
            good_guess = check_guess(guess)
            if good_guess:
                break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")


def check_guess(guess):
    guess = guess.lower()

    if guess in word:
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False
