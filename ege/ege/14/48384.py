from string import digits

alph = digits[:9]

for x in alph:
    for y in alph:
        res = int('88' + x + '4' + y, 9) + int('7' + x + '44' + y, 11)

        if res%61 == 0:
            print(res//61)