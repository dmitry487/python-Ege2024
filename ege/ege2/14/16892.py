num = 125 ** 4 + 25 ** 8 - 30


cifri = []


while num > 0:
    cifri.append(num%5)
    num//= 5


print(cifri.count(4))