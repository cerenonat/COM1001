# 2.14 (Target Heart-Rate Calculator)
# Calculate maximum heart rate and target heart rate range.

age = int(input('Enter your age: '))

max_heart_rate = 220 - age
target_lower = max_heart_rate * 0.5
target_upper = max_heart_rate * 0.85

print('Maximum heart rate:', max_heart_rate)
print('Target heart rate range:', f'{target_lower:.0f} - {target_upper:.0f}')
