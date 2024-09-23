from string import digits, ascii_lowercase

alph = digits + ascii_lowercase[:2]

for x in alph:
    for y in alph:
        res = int(y + 'aa' + x, 12) + int(x + '02' + y, 14)

        if res%80 == 0:
            print(res//80)