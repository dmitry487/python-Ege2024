num = 216**6 + 216 **  4 +  36 ** 6 - 6 ** 14 - 24


cislo = set()

while num > 0:
    cislo.add(num%6)
    num//=6

print(cislo)