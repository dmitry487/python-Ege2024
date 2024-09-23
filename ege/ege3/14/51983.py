from string import digits, ascii_lowercase

alph = digits + ascii_lowercase[:27]



for x in alph:
    res = int('123' + x, 37) + int('4' + x + '59', 37)


    if res%36 == 0:
        print(res//36)
        