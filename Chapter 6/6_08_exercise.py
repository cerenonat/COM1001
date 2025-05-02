
# 6.8 (Check Amount to Words)
# Create a dictionary that maps numbers to their corresponding word equivalents.

def check_amount_to_words(amount):
    ones = ['', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
    teens = ['TEN', 'ELEVEN', 'TWELVE', 'THIRTEEN', 'FOURTEEN', 'FIFTEEN', 'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN']
    tens = ['', '', 'TWENTY', 'THIRTY', 'FORTY', 'FIFTY', 'SIXTY', 'SEVENTY', 'EIGHTY', 'NINETY']

    def two_digit_word(n):
        if 10 <= n < 20:
            return teens[n-10]
        elif n >= 20:
            return tens[n//10] + ('' if n % 10 == 0 else ' ' + ones[n % 10])
        else:
            return ones[n]

    def three_digit_word(n):
        word = ''
        if n >= 100:
            word += ones[n//100] + ' HUNDRED '
            n %= 100
        if n:
            word += two_digit_word(n)
        return word.strip()

    dollars = int(amount)
    cents = round((amount - dollars) * 100)
    return f"{three_digit_word(dollars)} AND {cents:02d}/100"

print(check_amount_to_words(112.43))
