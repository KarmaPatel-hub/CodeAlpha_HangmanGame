## Hangman Game 

import random

# words list
words = ["planet", "dragon", "guitar", "rocket", "camera"]

secret_word = random.choice(words)

display = []

for i in secret_word:
    display.append("_")

lives = 6

print("Welcome to Hangman Game")

while lives > 0 and "_" in display:

    print("\nWord:", " ".join(display))
    print("Lives left:", lives)

    guess = input("Enter a letter: ").lower()

    correct = False

    for position in range(len(secret_word)):

        if secret_word[position] == guess:
            display[position] = guess
            correct = True

    if correct == False:
        lives -= 1
        print("Wrong Guess")

    else:
        print("Correct Guess")

if "_" not in display:
    print("\nYou Win!")
    print("Word was:", secret_word)

else:
    print("\nYou Lose!")
    print("Word was:", secret_word)