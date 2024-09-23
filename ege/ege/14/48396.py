from string import digits, ascii_lowercase

alph = digits + ascii_lowercase[:6]

for x in alph:
    res = int('2' + x + '84', 19) + int('2' + 'b' + '3' + x, 16)

    if res%88 == 0:
        print(res//88)