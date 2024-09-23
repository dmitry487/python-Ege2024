num = 49 ** 6 + 7 ** 18 - 21


cifri = []

while num > 0:
    cifri.append(num%7)
    num//=7

print(cifri.count(6))