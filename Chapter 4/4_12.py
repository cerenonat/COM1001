# 4.12 Simulation: Tortoise and Hare Race
import random
import time

def move_tortoise(position):
    move = random.randint(1, 10)
    if move <= 5:
        position += 3  # Fast plod
    elif move <= 7:
        position -= 6  # Slip
    else:
        position += 1  # Slow plod
    return max(1, position)

def move_hare(position):
    move = random.randint(1, 10)
    if move <= 2:
        pass  # Sleep
    elif move <= 4:
        position += 9  # Big hop
    elif move == 5:
        position -= 12  # Big slip
    elif move <= 8:
        position += 1  # Small hop
    else:
        position -= 2  # Small slip
    return max(1, position)

def race():
    tortoise = hare = 1
    print("BANG !!!!!\nAND THEY'RE OFF !!!!!")
    while tortoise < 70 and hare < 70:
        tortoise = move_tortoise(tortoise)
        hare = move_hare(hare)
        track = [' '] * 70
        if tortoise == hare:
            track[tortoise-1] = 'OUCH!!!'
        else:
            if tortoise <= 70:
                track[tortoise-1] = 'T'
            if hare <= 70:
                track[hare-1] = 'H'
        print(''.join(f'{t:<8}' for t in track))
        time.sleep(0.2)
    if tortoise >= 70 and hare >= 70:
        print("It's a tie!")
    elif tortoise >= 70:
        print("TORTOISE WINS!!! YAY!!!")
    else:
        print("Hare wins. Yuch.")

# Uncomment to run the race
# race()
