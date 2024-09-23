num = 9 ** 7 + 3 ** 21 - 9

cifri = []

while num > 0:
    cifri.append(num%3)
    num//=3

print(cifri.count(2))