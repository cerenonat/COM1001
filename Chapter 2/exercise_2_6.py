# 2.6 (Odd or Even)
# Determine whether an integer is odd or even.

number = int(input('Enter an integer: '))

if number % 2 == 0:
    print(number, 'is even.')
if number % 2 != 0:
    print(number, 'is odd.')
