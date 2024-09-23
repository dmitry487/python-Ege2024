from string import digits, ascii_lowercase


alph = digits + ascii_lowercase[:3]


for x in alph:
    for y in alph:
        res = int('4' + 'c' + x + '4', 15) + int(x + '62a', 13)


        if res%121 == 0:
            print(res//121)