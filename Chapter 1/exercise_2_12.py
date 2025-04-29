# 2.12 (7% Investment Return)
# Calculate how much money you'll have after 10, 20, and 30 years.

p = 1000
r = 0.07

for n in [10, 20, 30]:
    a = p * (1 + r) ** n
    print(f'After {n} years: ${a:.2f}')
