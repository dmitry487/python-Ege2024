num = 4 * 625 ** 9 - 25 ** 15 + 2 * 5 ** 11 - 7

cifri = []

while num > 0:
    cifri.append(num%5)
    num//=5

print(cifri.count(4))