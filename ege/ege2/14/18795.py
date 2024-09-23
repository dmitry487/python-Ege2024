num = 5 ** 36 + 5 ** 24 - 25

cifri = []

while num > 0:
    cifri.append(num%5)
    num//=5

print(cifri.count(4))