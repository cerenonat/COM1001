def character_counts(sentence):
    sentence = sentence.replace(" ", "").lower()
    counter = {}

    for char in sentence:
        if char.isalpha():
            counter[char] = counter.get(char, 0) + 1

    print("Letter  Count")
    for char in sorted(counter):
        print(f"{char:<7}{counter[char]}")

    # Challenge: Hangi harfler kullanılmamış?
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used = set(counter.keys())
    missing = alphabet - used
    print("\nMissing letters:", "".join(sorted(missing)))

# Örnek test
character_counts("To be or not to be that is the question")
