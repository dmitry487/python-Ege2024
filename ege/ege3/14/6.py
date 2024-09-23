num = 7 * 512 ** 1912 + 6 * 64 ** 1954 - 5 * 8 ** 1991 - 4 * 8 ** 1980 - 2022


cifri = []


while num > 0:
    cifri.append(num%8)
    num//=8



print(cifri.count(7))