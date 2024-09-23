num = 36 ** 7 + 6 ** 19 - 18


cifri = []



while num > 0:
    cifri.append(num%6)
    num//=6


print(cifri.count(5))