from string import digits, ascii_lowercase


alph = digits, ascii_lowercase[:3]


for x in alph:
    for y in alph:
        res = int('8' + x + '78' + y, 13) + int('79' + x + y + '7', 18)


        if res%9 == 0:
            print(res//9)