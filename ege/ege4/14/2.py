num = 18 * 7 ** 108 - 5 * 49 ** 76 + 343 ** 35 - 50
num = abs(num)

cifri = []


while num > 0:
    cifri.append(num%49)
    num//=49


print(sum(cifri))