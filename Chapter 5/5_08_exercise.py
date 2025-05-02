# 5.8 (Sieve of Eratosthenes)
primes = [True] * 1000
primes[0:2] = [False, False]

for i in range(2, int(1000**0.5)+1):
    if primes[i]:
        for j in range(i*i, 1000, i):
            primes[j] = False

prime_numbers = [i for i, is_prime in enumerate(primes) if is_prime]
print(prime_numbers)
