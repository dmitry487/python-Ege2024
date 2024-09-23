num = 49 ** 7 + 7 ** 21 - 7

cifri = []


while num > 0:
    cifri.append(num%7)
    num//=7

print(cifri.count(6))