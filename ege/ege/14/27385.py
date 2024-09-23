num = 343 ** 5 + 343 ** 4 + 49 ** 6 - 7 ** 13 - 21

cifri = set()


while num > 0:
    cifri.add(num%7)
    num//= 7

print(cifri)