from string import digits, ascii_lowercase

alph = digits + ascii_lowercase[:12]
kolichestvo = 0
for x in alph:
    res = int('63' + x + '59685', 22) + int('17' + x + '53', 22) + int('36' + x + '5', 22)
    if res%21 == 0:
        print(res//21)
