num = 3 * 343 ** 8 + 5 * 49 ** 12 + 7 ** 15 - 49

cifri = []


while num > 0:
    cifri.append(num%7)
    num//=7

print(cifri.count(6))
print(cifri.count(0))