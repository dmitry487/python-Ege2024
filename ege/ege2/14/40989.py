num = 2 * 216 ** 8 + 4 * 36 ** 12 + 6 ** 15 - 1296

cifri = []

while num > 0:
    cifri.append(num%6)
    num//=6

print(cifri.count(0))