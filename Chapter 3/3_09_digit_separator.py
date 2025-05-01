# 3.9 Separating Digits
number = int(input("Enter a five-digit integer: "))

for divisor in [10000, 1000, 100, 10, 1]:
    print(number // divisor, end=' ')
    number %= divisor
print()
