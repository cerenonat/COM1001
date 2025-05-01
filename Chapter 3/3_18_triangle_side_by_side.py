# 3.18 Side-by-Side Triangles
for i in range(1, 11):
    line = ''
    line += '*' * i
    line += ' ' * 3
    line += '*' * (11 - i)
    line += ' ' * 3
    line += ' ' * (i - 1) + '*' * (11 - i)
    line += ' ' * 3
    line += ' ' * (10 - i) + '*' * i
    print(line)
