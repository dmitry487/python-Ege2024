from string import digits, ascii_lowercase


alph = digits + ascii_lowercase[:5]


for x in alph:
    res = int('123' + x + '5', 15) + int('1' + x + '233', 15)

    if res%14 == 0:
        print(res//14)