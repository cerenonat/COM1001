# 3.27 World Population Growth
population = 8_000_000_000  # example
rate = 0.01  # 1% growth
for year in range(1, 101):
    increase = population * rate
    population += increase
    print(f"{year:3d} {int(population):>15,d} {int(increase):>15,d}")
