num = 9 ** 11 * 3 ** 20 - 3 ** 9 - 27

cifri = []

while num > 0:
    cifri.append(num%3)
    num//=3

print(cifri.count(2))