# 5.10 (Anagrams)
def anagrams(s):
    if len(s) <= 1:
        return [s]
    result = []
    for i, letter in enumerate(s):
        for perm in anagrams(s[:i] + s[i+1:]):
            result.append(letter + perm)
    return result

print(anagrams("bat"))
