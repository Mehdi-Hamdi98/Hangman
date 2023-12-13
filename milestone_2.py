import random
import string

word_list = ["banana", "apple", "mango", "orange", "grapes"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Enter a single letter: ")


if len(guess) == 1 and guess in string.ascii_letters:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
