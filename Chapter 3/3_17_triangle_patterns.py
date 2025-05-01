# 3.17 Triangle Patterns
for i in range(1, 11):
    print('*' * i)

print()

for i in range(10, 0, -1):
    print('*' * i)

print()

for i in range(10, 0, -1):
    print(' ' * (10 - i) + '*' * i)

print()

for i in range(1, 11):
    print(' ' * (10 - i) + '*' * i)
