num = 4 ** 34 + 5 * 4** 22 + 4 ** 13 + 2 * 4 ** 9 + 82

cifri = set()

while num > 0:
    cifri.add(num%16)
    num//=16

print(cifri)