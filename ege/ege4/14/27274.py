num = 16 ** 5 + 8 ** 6 + 4 ** 9 - 128


cifri = []


while num > 0:
    cifri.append(num%2)
    num//=2


print(cifri.count(1))