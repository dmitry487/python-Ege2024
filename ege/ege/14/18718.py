num = 4 ** 1014 + 2 ** 1012 - 7

cifri = []

while num > 0:
    cifri.append(num%2)
    num//= 2

print(cifri.count(1))