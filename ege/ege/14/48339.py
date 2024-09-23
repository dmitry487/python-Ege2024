from string import digits, ascii_lowercase

alph = ascii_lowercase + digits[:1]

for x in alph:
    for y in alph:
        res = int('982' + x + '8', 11) + int('194' + x + '7', 11)

        if res%58 == 0:
            print(res//58)