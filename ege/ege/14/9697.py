num = 4 ** 2016 + 2 ** 2015 - 7

cifri = []

while num > 0:
    cifri.append(num%2)
    num//=2


print(cifri.count(1))