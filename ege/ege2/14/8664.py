num = 8 ** 2020 + 4 ** 2017 + 26 - 1

cifri =[]


while num > 0:
    cifri.append(num%2)
    num//=2


print(cifri.count(1))