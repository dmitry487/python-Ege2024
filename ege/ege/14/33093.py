num = 81 ** 15 + 3 ** 22 - 27

cifri = []

while num > 0:
    cifri.append(num%9)
    num//=9

print(cifri.count(8))