# 3.8 Arithmetic, Smallest and Largest
total = 0
smallest = None
largest = None

for _ in range(4):
    number = int(input("Enter an integer: "))
    total += number
    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number

print(f"Sum: {total}")
print(f"Average: {total / 4}")
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
