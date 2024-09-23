num = 729 ** 8 - 3 ** 18 + 85

cifri = []

while num > 0:
    cifri.append(num%9)
    num//=9

print(cifri.count(0))