num = 4* 16 + 2 * 36 - 16


cifri = []

while num > 0:
    cifri.append(num%2)
    num//= 2

print(cifri.count(1))
print(cifri)