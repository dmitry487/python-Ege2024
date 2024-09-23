num = 4 ** 8 + 2 ** 8 - 8


cifri = []

while num > 0:
    cifri.append(num%2)
    num//=2

print(cifri.count(1))