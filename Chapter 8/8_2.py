# 8.2 (Random Sentences)

import random

article = ["the", "a", "one", "some", "any"]
noun = ["boy", "girl", "dog", "town", "car"]
verb = ["drove", "jumped", "ran", "walked", "skipped"]
preposition = ["to", "from", "over", "under", "on"]

for _ in range(20):
    sentence = " ".join([
        random.choice(article),
        random.choice(noun),
        random.choice(verb),
        random.choice(preposition),
        random.choice(article),
        random.choice(noun)
    ])
    sentence = sentence.capitalize() + "."
    print(sentence)
