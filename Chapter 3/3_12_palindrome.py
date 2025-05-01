# 3.12 Palindrome
number = int(input("Enter a five-digit integer: "))

if number < 10000 or number > 99999:
    print("Invalid input. Must be five digits.")
else:
    original = number
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10

    if original == reverse:
        print("It's a palindrome.")
    else:
        print("It's not a palindrome.")
