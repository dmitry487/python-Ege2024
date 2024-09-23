from string import digits, ascii_lowercase


alph = digits + ascii_lowercase[:22]


for x in alph:
    p = x ** 5
    res = int('72' + x, 32) + int('1c' + x + '7', 32) + int(p, 32)

    if res%x == 0:
        print(x)
