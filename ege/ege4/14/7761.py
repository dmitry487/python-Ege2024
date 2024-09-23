num = 4 ** 2020 + 2 ** 2017 - 15


cifri = []


while num > 0:
    cifri.append(num%2)
    num//=2


print(cifri.count(1))