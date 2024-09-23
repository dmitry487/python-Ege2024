num = 2 * 216 ** 6 + 3 * 36 **9 - 432


cifri = []



while num > 0:
    cifri.append(num%6)
    num//=6


print(cifri.count(5))