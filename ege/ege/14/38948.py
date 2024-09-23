num = 4 ** 36 + 3 * 4 ** 20 + 4 ** 15 + 2 * 4 ** 7 + 49

cifri = set()

while num > 0:
    cifri.add(num%16)
    num//= 16

print(cifri)