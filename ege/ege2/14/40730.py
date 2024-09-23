num = 3 * 125 ** 6 + 2 * 25 ** 9 + 5 ** 12 - 625


cifri = []


while num > 0:
    cifri.append(num%5)
    num//= 5


print(cifri.count(0))