num = 3 * 4 ** 38 + 2 * 4 ** 23 + 4 ** 20 + 3 * 4 ** 5 + 2 * 4 ** 4 + 1

cifri = []

while num > 0:
    cifri.append(num%16)
    num//= 16

print(cifri.count(0))