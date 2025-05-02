# 5.5 (Slicing Operations)
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# a) The first half using start and end indices
print("a)", alphabet[0:13])

# b) The first half using only the end index
print("b)", alphabet[:13])

# c) The second half using start and end indices
print("c)", alphabet[13:26])

# d) The second half using only the start index
print("d)", alphabet[13:])

# e) Every second letter starting with 'a'
print("e)", alphabet[::2])

# f) Entire string in reverse
print("f)", alphabet[::-1])

# g) Every third letter in reverse starting with 'z'
print("g)", alphabet[::-3])
