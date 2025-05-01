# 3.21 Calculate Change
cost = float(input("Enter purchase price (under $1): "))
change = round(1.00 - cost, 2)
cents = int(change * 100)

quarters = cents // 25
cents %= 25
dimes = cents // 10
cents %= 10
nickels = cents // 5
pennies = cents % 5

print("Your change is:")
if quarters: print(quarters, "quarters")
if dimes: print(dimes, "dimes")
if nickels: print(nickels, "nickels")
if pennies: print(pennies, "pennies")
