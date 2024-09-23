from string import digits, ascii_lowercase


alph = digits + ascii_lowercase[:7]


for x in alph:
    res = int('10' + x + '0', 17) + int('f0' + x + 'ff', 17)

    if res%13 == 0:
        print(res//13)