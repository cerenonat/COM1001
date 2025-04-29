# 2.10 (Arithmetic, Smallest and Largest)
# Input three integers and display sum, average, product, smallest and largest.

a = int(input('Enter first integer: '))
b = int(input('Enter second integer: '))
c = int(input('Enter third integer: '))

print('Sum:', a + b + c)
print('Average:', (a + b + c) / 3)
print('Product:', a * b * c)
print('Smallest:', min(a, b, c))
print('Largest:', max(a, b, c))
