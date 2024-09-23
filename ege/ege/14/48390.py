from string import digits

alph = digits[:8]

for x in alph:
    for y in alph:
        res = int(x + '01' + y + '4', 9) + int(x + y + '544', 8)
        if res%89 == 0:
            print(res/89)