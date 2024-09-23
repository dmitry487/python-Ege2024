num = 5 * 3 ** 1917 + 6 * 2 ** 1878 + 7 * 3 ** 1870 - 1991

cifri = []

while num > 0:
    cifri.append(num%17)
    num//=17

for i in range (0, 16):
    print(cifri.count(i), i)
    i += 1

