from string import digits,ascii_lowercase

alph = digits + ascii_lowercase

for p in alph:
    for x in alph:
        for y in alph:
            for z in alph:
                if int(y + '4' + y, p) + int(y + '65', p) == int(x + z + '23', p):
                    print(x + y + z, p)