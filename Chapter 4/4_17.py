# 4.17 Computer-Assisted Instruction: Varying the Types of Problems
import random

def generate_question(problem_type):
    if problem_type == 1:
        x, y = random.randint(1, 9), random.randint(1, 9)
        return x, y, '+', x + y
    elif problem_type == 2:
        x, y = random.randint(1, 9), random.randint(1, 9)
        return x, y, '-', x - y
    elif problem_type == 3:
        x, y = random.randint(1, 9), random.randint(1, 9)
        return x, y, '*', x * y
    elif problem_type == 4:
        x, y = random.randint(1, 9), random.randint(1, 9)
        return x * y, y, '/', x
    else:  # random
        return generate_question(random.randint(1, 4))

def practice():
    ptype = int(input("Choose problem type (1:add 2:sub 3:mul 4:div 5:random): "))
    while True:
        x, y, op, correct = generate_question(ptype)
        while True:
            answer = int(input(f"What is {x} {op} {y}? "))
            if answer == correct:
                print("Very good!")
                break
            else:
                print("No. Please try again.")

# Uncomment to practice
# practice()
