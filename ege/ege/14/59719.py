from string import digits, ascii_lowercase

alph = digits + ascii_lowercase[:5]

for x in alph:
    res = int('98' + x + '79641', 22) + int('25' + x + '49', 22) + int('63' + x + '5', 22)


    if (res%21) == 0:
        print(res/21)

