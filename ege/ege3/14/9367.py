num = 9 **8 + 2 ** 5 - 9


cifri = []



while num > 0:
    cifri.append(num%3)
    num//=3


print(cifri.count(2))