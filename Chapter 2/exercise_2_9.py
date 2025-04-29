# 2.9 (Integer Value of a Character)
# Display the integer equivalents of B C D b c d 0 1 2 $ * + and space.

characters = ['B', 'C', 'D', 'b', 'c', 'd', '0', '1', '2', '$', '*', '+', ' ']

for char in characters:
    print(f"'{char}' = {ord(char)}")
