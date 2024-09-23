from string import digits


alph = digits[:9]


for x in alph:
    res = int('88' + x + '4' + x, 9) + int('7' + x + '344', 9)


    if res%67 == 0:
        print(res//67)