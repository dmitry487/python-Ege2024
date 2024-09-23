from string import digits, ascii_lowercase


alph = digits + ascii_lowercase[:12]



for x in alph:
    res = int('98' + x + '79641', 22) + int('36' + x + '14', 22) + int('73' + x + '4', 22)


    if res%21 == 0:
        print(res//21)