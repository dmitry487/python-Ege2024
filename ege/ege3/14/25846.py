num = 9 ** 8 * 3 ** 20 - 3 ** 10 - 3


cifri = []


while num > 0:
    cifri.append(num%3)
    num//=3


print(cifri.count(2))