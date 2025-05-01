# 3.1 Validating User Input
passes = 0

for _ in range(10):
    result = int(input("Enter result (1=pass, 2=fail): "))
    while result != 1 and result != 2:
        result = int(input("Invalid input. Enter result (1=pass, 2=fail): "))
    if result == 1:
        passes += 1

failures = 10 - passes
print(f"Passed: {passes}")
print(f"Failed: {failures}")
