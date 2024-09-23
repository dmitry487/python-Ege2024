num = 4 ** 12 + 2 ** 32 - 16

cifri = []


while num > 0:
    cifri.append(num%2)
    num//=2

print(cifri.count(1))