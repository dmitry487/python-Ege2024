num = 4 * 343 ** 5 + 6 * 49 ** 8 - 50

cifri = []

while num > 0:
    cifri.append(num%7)
    num//=7

print(cifri.count(6))