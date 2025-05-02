# 5.12 (Telephone-Number Word Generator)
from itertools import product

keypad = {
    '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL',
    '6': 'MNO', '7': 'PRS', '8': 'TUV', '9': 'WXY'
}

def phone_to_words(number):
    if any(d in '01' for d in number):
        return []
    letters = [keypad[d] for d in number]
    return [''.join(p) for p in product(*letters)]

print(phone_to_words("6862377"))
