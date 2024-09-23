from string import digits,ascii_lowercase


alph = digits + ascii_lowercase[:9]


for x in alph:
    res = int('98897' + x + '21', 19) + int('2' + x + '923', 19)

    if res%18 == 0:
        print(res//18)