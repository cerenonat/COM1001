# 3.20 Binary to Decimal
binary = input("Enter a binary number: ")
decimal = 0
for i, digit in enumerate(reversed(binary)):
    decimal += int(digit) * (2 ** i)
print(f"Decimal equivalent: {decimal}")
