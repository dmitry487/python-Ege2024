num = 4 ** 14 + 2 ** 32 - 4


cifri = []


while num > 0:
    cifri.append(num%2)
    num//= 2


print(cifri.count(1))