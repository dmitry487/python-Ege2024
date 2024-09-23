from string import digits, ascii_lowercase


alph = digits + ascii_lowercase[:9]



for x in alph:
    res = int('78' + x + '79643', 19) + int('25' + x + '43', 19) + int('63' + x + '5', 19)

    if res%18 == 0:
        print(res//18)