from string import digits, ascii_lowercase

alph = digits + ascii_lowercase[:2]

for x in alph:
    res = int('3' + x + 'da', 14) +\
    int('5' + x + 'a6', 12)

    if res%81 == 0:
        print(res//81)