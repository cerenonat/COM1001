def count_duplicates(sentence):
    words = sentence.lower().split()
    counter = {}

    for word in words:
        counter[word] = counter.get(word, 0) + 1

    duplicates = {word: count for word, count in counter.items() if count > 1}
    
    print("Duplicate words:")
    for word, count in duplicates.items():
        print(f'{word:<12}{count}')

# Örnek test
count_duplicates("To be or not to be that is the question")
