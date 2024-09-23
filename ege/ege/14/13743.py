num = 49 ** 10 + 7 ** 30 - 49

cifri = []

while num > 0:
    cifri.append(num%7)
    num//=7

print(cifri.count(6))