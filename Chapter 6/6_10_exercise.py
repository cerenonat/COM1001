# 6.10 (Set Manipulations)
s1 = {'red', 'green', 'blue'}
s2 = {'cyan', 'green', 'blue', 'magenta', 'red'}

# a) Comparisons
print(s1 <= s2)  # True (subset)
print(s1 < s2)   # True (proper subset)
print(s1 >= s2)  # False
print(s1 > s2)   # False

# b) Set operations
print(s1 | s2)  # Union
print(s1 & s2)  # Intersection
print(s1 - s2)  # Difference
print(s1 ^ s2)  # Symmetric Difference
