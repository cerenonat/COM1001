def unique_words(sentence):
    words = sentence.lower().split()
    unique = sorted(set(words))
    
    print("Unique words:")
    for word in unique:
        print(word)

# Örnek test
unique_words("To be or not to be that is the question")
