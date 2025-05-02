# 5.7 (Duplicate Elimination)
def unique_sorted(lst):
    return sorted(set(lst))

print(unique_sorted([4, 6, 2, 4, 1, 2]))
print(unique_sorted(["apple", "banana", "apple", "cherry"]))
