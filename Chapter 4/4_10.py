# 4.10 Guess the Number
import random

def guess_number():
    number = random.randint(1, 1000)
    print("Guess my number between 1 and 1000 with the fewest guesses:")
    guess = 0
    while guess != number:
        guess = int(input("Your guess: "))
        if guess > number:
            print("Too high. Try again.")
        elif guess < number:
            print("Too low. Try again.")
        else:
            print("Congratulations. You guessed the number!")

guess_number()
