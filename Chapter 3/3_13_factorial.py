# 3.13 Factorials
n = int(input("Enter a nonnegative integer: "))
result = 1

for i in range(2, n + 1):
    result *= i

print(f"{n}! is {result}")
