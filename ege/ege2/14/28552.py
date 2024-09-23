num = 216 ** 6 + 216 ** 4 + 36 ** 6 - 6 ** 14 - 24

cifri = set()

while num > 0:
    cifri.add(num%6)
    num//= 6

print(cifri)