num = 4 ** 255 + 2 ** 255 - 255

cifri = []

while num > 0:
    cifri.append(num%2)
    num//=2

print(cifri.count(1))