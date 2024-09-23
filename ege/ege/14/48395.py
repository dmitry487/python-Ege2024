from string import digits, ascii_lowercase

alph = digits + ascii_lowercase[:2]


for x in alph:
    res = int('28' + x + '2', 18) + int('93' + x + '5', 12)

    if res%133 == 0:
        print(res/133)
