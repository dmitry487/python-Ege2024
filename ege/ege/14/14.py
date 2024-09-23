from string import digits, ascii_lowercase
import math


alph = digits + ascii_lowercase[:40]
kolichestvo = 0
for x in alph:
    for y in alph:
        res = int('57' + x + '692' + y + '19', 40)
        res1 = int(x + y, 40)
        sqrt = math.sqrt(res1)
        if (res%39 == 0) and (sqrt == int):
            r = int(y + x, 2)
            print(r)

