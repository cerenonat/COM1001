# 3.16 Two Largest
largest = second = float('-inf')

for _ in range(10):
    number = int(input("Enter a number: "))
    if number > largest:
        second = largest
        largest = number
    elif number > second:
        second = number

print(f"Largest: {largest}")
print(f"Second largest: {second}")
