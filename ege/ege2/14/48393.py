from string import digits

alph = digits[:8]


for x in alph:
    for y in alph:
        res = int(y + '04' + x + '5', 11) + int('253' + x + y, 8)


        if res%117 == 0:
            print(res//117)