# 4.4 What Does This Code Do?
# Sums the squares of the elements of the list.
def mystery(x):
    y = 0
    for value in x:
        y += value ** 2
    return y

print(mystery([1, 2, 3, 4, 5]))  # Outputs 55
