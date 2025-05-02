# 5.11 (Summarizing Letters in a String)
def summarize_letters(s):
    s = ''.join(c.lower() for c in s if c.isalpha())
    summary = {}
    for ch in s:
        summary[ch] = summary.get(ch, 0) + 1
    result = sorted(summary.items())
    for k, v in result:
        print(f"{k}: {v}")
    if len(summary) == 26:
        print("Contains all letters of the alphabet.")
    else:
        print("Missing letters.")

summarize_letters("The quick brown fox jumps over a lazy dog")
