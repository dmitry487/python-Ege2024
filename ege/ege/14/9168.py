num = 16 ** 2018 + 4 ** 2018 + 25 - 1

cifir = []

while num > 0:
    cifir.append(num%2)
    num//=2

print(cifir.count(1))