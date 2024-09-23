num = 9**2016 + 3 ** 2015 - 9

cifri = []


while num > 0:
    cifri.append(num%3)
    num//=3

print(cifri.count(2))