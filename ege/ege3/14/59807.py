from string import ascii_lowercase, digits


alph = digits + ascii_lowercase[:15]



for x in alph:
    res = int('8' + x + '5678', 25) + int('457' + x + '69', 25) +\
    int('145' + x + '1', 25)


    if res%23 == 0:
        print(res//23)