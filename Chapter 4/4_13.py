# 4.13 Arbitrary Argument List
def product(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

print(product(2, 3, 4))  # 24
print(product(5, 5))     # 25
