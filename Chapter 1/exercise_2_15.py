# 2.15 (Sort in Ascending Order)
# Input three floating-point numbers and display them in ascending order.

numbers = []

for _ in range(3):
    num = float(input('Enter a floating-point number: '))
    numbers.append(num)

numbers.sort()

print('Numbers in ascending order:', numbers)
