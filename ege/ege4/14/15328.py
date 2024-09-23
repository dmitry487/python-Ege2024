from string import digits, ascii_lowercase


alph = digits + ascii_lowercase[:17]


for x in alph:
    res = int('123' + x + '24', 27) + int('135' + x + '78', 27)



    if res%26 == 0:
        print(res//26)
        