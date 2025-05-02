# 6.9 (Dictionary Manipulations)
tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

# a)
print('Canada' in tlds)  # True
# b)
print('France' in tlds)  # False
# c)
for country, domain in tlds.items():
    print(f"{country:<15} {domain}")
# d)
tlds['Sweden'] = 'sw'
# e)
tlds['Sweden'] = 'se'
# f)
reversed_tlds = {v: k for k, v in tlds.items()}
# g)
upper_countries = {k: v.upper() for k, v in reversed_tlds.items()}
print(upper_countries)
