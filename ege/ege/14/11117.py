num = 4 ** 2013 + 2 ** 2012 - 16

cifri = []


while num > 0:
    cifri.append(num%2)
    num//=2


print(cifri.count(1))