# 4.9 Temperature Conversion
def fahrenheit(celsius):
    return (9 / 5) * celsius + 32

print("Celsius  Fahrenheit")
for c in range(0, 101):
    print(f"{c:7} {fahrenheit(c):10.1f}")
