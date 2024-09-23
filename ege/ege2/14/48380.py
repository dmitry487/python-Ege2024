from string import digits, ascii_lowercase

alph = digits + ascii_lowercase[:2]


for x in alph:
    for a in alph:
        if int('49' + x + '26', 12) + int(a, 12)% int('49' + x + '70', 12) == 0:

            print(a)
        