from string import digits, ascii_lowercase


alph = digits + ascii_lowercase[:4]


for x in alph:
    res = int('1' + x + '563', 14) + int('871' + x + '3', 14)

    if res%24 == 0:
        print(res/24)