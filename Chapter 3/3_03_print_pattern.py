# 3.3 What Does This Code Do?
# Prints a 10x10 grid of '>' on even rows and '<' on odd rows.
for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
    print()
