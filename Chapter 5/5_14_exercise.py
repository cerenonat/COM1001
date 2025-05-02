# 5.14 (Is a Sequence Sorted?)
def is_ordered(seq):
    return list(seq) == sorted(seq)

print(is_ordered([1, 2, 3]))
print(is_ordered([3, 1, 2]))
print(is_ordered("abc"))
