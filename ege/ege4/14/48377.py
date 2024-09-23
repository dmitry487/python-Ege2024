from string import digits, ascii_lowercase


alph = digits + ascii_lowercase[:3]



for x in alph:
    res = int('26' + x + '98', 13) + int('4'+ x + '296', 13)


    if res%34 == 0:
        print(res//34)