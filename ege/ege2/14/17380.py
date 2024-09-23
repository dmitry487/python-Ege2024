num = 3 * 216 ** 4 + 2 * 36 ** 6 - 648

cifri = []



while num > 0:
    cifri.append(num%6)
    num//=6


print(cifri.count(5))   