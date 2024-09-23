num = 729 ** 7 + 3 ** 16 - 18

cifri = []


while num > 0:
    cifri.append(num%9)
    num//=9


print(cifri.count(0))