from string import digits, ascii_lowercase


alph = digits + ascii_lowercase[:3]

for x in alph:
    res = int('8' + x + '71', 13) + int('3' + x + 'df', 17)

    if res%197 == 0:
        print(res/197)