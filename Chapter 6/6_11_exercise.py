# 6.11 (Craps Simulation Summary)
import random

wins = {}
losses = {}

GAMES = 1_000_000

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

for _ in range(GAMES):
    roll_count = 1
    sum_of_dice = roll_dice()
    if sum_of_dice in (7, 11):
        wins[roll_count] = wins.get(roll_count, 0) + 1
    elif sum_of_dice in (2, 3, 12):
        losses[roll_count] = losses.get(roll_count, 0) + 1
    else:
        point = sum_of_dice
        while True:
            roll_count += 1
            sum_of_dice = roll_dice()
            if sum_of_dice == point:
                wins[roll_count] = wins.get(roll_count, 0) + 1
                break
            elif sum_of_dice == 7:
                losses[roll_count] = losses.get(roll_count, 0) + 1
                break

total_wins = sum(wins.values())
total_losses = sum(losses.values())
total_games = total_wins + total_losses

print(f"Percentage of wins: {total_wins / total_games * 100:.1f}%")
print(f"Percentage of losses: {total_losses / total_games * 100:.1f}%")

print(f"{'Rolls':<6}{'% Resolved':<15}{'Cumulative %'}")
cumulative = 0
for roll in sorted(set(wins) | set(losses)):
    resolved = wins.get(roll, 0) + losses.get(roll, 0)
    percent = resolved / total_games * 100
    cumulative += percent
    print(f"{roll:<6}{percent:<15.2f}{cumulative:.2f}%")
