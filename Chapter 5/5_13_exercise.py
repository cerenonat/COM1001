# 5.13 (Word or Phrase to Phone-Number Generator)
letter_to_digit = {letter: digit for digit, letters in keypad.items() for letter in letters}

def word_to_phone(word):
    return ''.join(letter_to_digit.get(ch.upper(), '?') for ch in word)

print(word_to_phone("NUMBERS"))
