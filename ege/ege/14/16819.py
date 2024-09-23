num = 125 ** 5 + 25 ** 9 - 30

cifri = []

while num > 0:
    cifri.append(num%5)
    num//=5

print(cifri.count(4))