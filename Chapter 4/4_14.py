# 4.14 Computer-Assisted Instruction
import random

def generate_question():
    return random.randint(1, 9), random.randint(1, 9)

def multiplication_practice():
    while True:
        x, y = generate_question()
        while True:
            answer = int(input(f"How much is {x} times {y}? "))
            if answer == x * y:
                print("Very good!")
                break
            else:
                print("No. Please try again.")

# Uncomment to practice
# multiplication_practice()
