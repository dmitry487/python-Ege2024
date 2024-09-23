from string import digits, ascii_lowercase

alph = digits + ascii_lowercase[:2]


for x in alph:
    for y in alph:
        res = int(x + '231' + y, 12) + int('78' + x + '98' + y, 14)

        if res%99 == 0:
            print(res/99)