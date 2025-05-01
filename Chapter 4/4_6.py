# 4.6 Modified average Function
def average(first, *args):
    return (first + sum(args)) / (1 + len(args))

print(average(10, 20, 30))  # 20.0
