from string import digits


alph = digits[:9]

for a in range (1000):
    for x in alph:
        m = int('842' + x + '5', 9)
        n = int('8' + x + '725', 9)


        if (m + a)%n == 0:
            print(a, x)
            
