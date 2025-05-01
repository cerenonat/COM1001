# 8.3 (Pig Latin Translator)

def pig_latin(word):
    vowels = "aeiou"
    if word[0].lower() in vowels:
        return word + "ay"
    else:
        return word[1:] + word[0] + "ay"

phrase = input("Enter a phrase to convert to Pig Latin: ")
words = phrase.split()
translated = [pig_latin(word) for word in words]
print("Pig Latin:", " ".join(translated))
