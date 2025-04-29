# 2.11 (Separating the Digits in an Integer)
# Input a five-digit integer and separate the digits.

number = int(input('Enter a five-digit integer: '))

print(number // 10000, (number % 10000) // 1000, (number % 1000) // 100, (number % 100) // 10, number % 10)
