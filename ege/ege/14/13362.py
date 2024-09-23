num = 125 + 25 ** 3 + 5 ** 9

cifri = []

while num > 0:
    cifri.append(num%5)
    num//=5

print(cifri.count(0))