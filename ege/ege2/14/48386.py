from string import digits, ascii_lowercase

alph = digits + ascii_lowercase[:5]


for x in alph:
    for y in alph:
        res = int('90' + x + '4' + y, 15) + int('91' + x + y + '2', 16)

        if res%56 == 0:
            print(res//56)