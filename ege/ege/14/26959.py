num = 16**8 + 4 ** 10 - 4 ** 6 - 16

cifri = []

while num > 0:
    cifri.append(num%4)
    num//=4

print(cifri.count(3))