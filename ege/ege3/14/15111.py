num = 25 ** 5 + 5 ** 14 - 5


cifri = []


while num > 0:
    cifri.append(num%5)
    num//=5


print(cifri.count(4))