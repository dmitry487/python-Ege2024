num = 49 ** 8 + 7 ** 24 - 7

cifri = []


while num > 0:
    cifri.append(num%7)
    num//=7


print(cifri.count(0))