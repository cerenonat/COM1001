# 3.14 Approximating Pi
terms = int(input("Enter number of terms: "))
pi = 0
for i in range(terms):
    pi += (-1) ** i / (2 * i + 1)

pi *= 4
print(f"Approximated value of pi: {pi}")
