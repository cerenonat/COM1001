# 4.15 Computer-Assisted Instruction: Reducing Fatigue
import random

def positive_feedback():
    return random.choice(["Very good!", "Nice work!", "Keep up the good work!"])

def negative_feedback():
    return random.choice(["No. Please try again.", "Wrong. Try once more.", "No. Keep trying."])

def multiplication_practice():
    while True:
        x, y = random.randint(1, 9), random.randint(1, 9)
        while True:
            answer = int(input(f"How much is {x} times {y}? "))
            if answer == x * y:
                print(positive_feedback())
                break
            else:
                print(negative_feedback())

# Uncomment to practice
# multiplication_practice()
