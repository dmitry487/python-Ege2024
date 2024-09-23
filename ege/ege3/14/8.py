from string import digits, ascii_lowercase


alph = digits + ascii_lowercase



res = int('AB' + '267' + 'D' + '1', alph) + int('F' + '024' + 'A' + '89', alph)

if res%(alph - 1) == 0:
    print(alph)
    