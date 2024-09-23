num = 4 ** 511 + 2 ** 511 - 511


cifri = []


while num > 0:
    cifri.append(num%2)
    num//=2

print(cifri.count(1))