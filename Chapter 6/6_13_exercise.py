# 6.13 (Synonyms Dictionary)
synonyms = {
    'happy': ['joyful', 'cheerful', 'content'],
    'sad': ['unhappy', 'sorrowful', 'dejected'],
    'fast': ['quick', 'swift', 'rapid'],
    'smart': ['intelligent', 'clever', 'bright'],
    'strong': ['powerful', 'robust', 'sturdy']
}

for word, syns in synonyms.items():
    print(f"{word}:")
    for s in syns:
        print(f"  - {s}")
