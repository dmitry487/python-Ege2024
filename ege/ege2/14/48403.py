from string import digits, ascii_lowercase

alph = digits + ascii_lowercase[:2]


for x in alph:
    res = int('2ab' + x, 12) + int(x + '8e', 17)


    if res%27 == 0:
        print(res//27)