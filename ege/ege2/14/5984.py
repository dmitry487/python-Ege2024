num = 9 ** 12 + 3 ** 8 - 3

cifri = []

while num > 0:
    cifri.append(num%3)
    num//=3

print(cifri.count(2))