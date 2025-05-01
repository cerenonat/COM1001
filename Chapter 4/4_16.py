# 4.16 Computer-Assisted Instruction: Difficulty Levels
import random

def generate_question(level):
    if level == 1:
        return random.randint(1, 9), random.randint(1, 9)
    else:
        return random.randint(10, 99), random.randint(10, 99)

def multiplication_practice():
    level = int(input("Enter difficulty level (1 or 2): "))
    while True:
        x, y = generate_question(level)
        while True:
            answer = int(input(f"How much is {x} times {y}? "))
            if answer == x * y:
                print("Very good!")
                break
            else:
                print("No. Please try again.")

# Uncomment to practice
# multiplication_practice()
