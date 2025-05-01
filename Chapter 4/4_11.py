# 4.11 Guess-the-Number Modification
import random

def guess_number():
    number = random.randint(1, 1000)
    count = 0
    print("Guess my number between 1 and 1000:")
    guess = 0
    while guess != number:
        guess = int(input("Your guess: "))
        count += 1
        if guess > number:
            print("Too high. Try again.")
        elif guess < number:
            print("Too low. Try again.")
        else:
            print("Congratulations. You guessed the number!")
            if count <= 10:
                print("Either you know the secret or you got lucky!")
            else:
                print("You should be able to do better!")

guess_number()
