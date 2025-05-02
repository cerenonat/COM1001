# 5.6 (Functions Returning Tuples)
def rotate(x, y, z):
    return (z, x, y)

a, b, c = 'Doug', 22, 1984
a, b, c = rotate(a, b, c)
print("1st call:", a, b, c)
a, b, c = rotate(a, b, c)
print("2nd call:", a, b, c)
a, b, c = rotate(a, b, c)
print("3rd call:", a, b, c)
