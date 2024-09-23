num = 25 ** 6 + 5 ** 18 - 5


cifri = []


while num > 0:
    cifri.append(num%5)
    num//=5


print(cifri.count(4))