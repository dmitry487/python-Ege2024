num = 6 * 343 ** 5  + 5 * 49 ** 7  - 50

cifri = []
while num > 0:
    cifri.append(num%7)
    num//=7


print(cifri.count(6))
    