# 3.15 Approximating e
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

e = sum(1 / factorial(i) for i in range(10))
print(f"Approximated value of e: {e}")
