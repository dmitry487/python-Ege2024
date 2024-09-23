num = 343 ** 5 - 7 **9 + 48



cifri = []



while num > 0:
    cifri.append(num%7)
    num//=7


print(cifri.count(6))