# 6.12 (Translation Dictionary)
translations = {
    'hello': 'hola',
    'world': 'mundo',
    'computer': 'ordenador',
    'book': 'libro',
    'language': 'idioma'
}

print(f"{'English':<10}{'Translation'}")
for eng, trans in translations.items():
    print(f"{eng:<10}{trans}")
