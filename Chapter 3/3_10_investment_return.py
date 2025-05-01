# 3.10 7% Investment Return
amount = 1000
rate = 0.07

for year in range(1, 31):
    amount *= (1 + rate)
    print(f"Year {year}: ${amount:.2f}")
