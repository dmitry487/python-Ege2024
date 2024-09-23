num = 7 * 512 ** 120 - 6 * 64 ** 100 + 8 ** 210 - 255


cifri = []


while num > 0:
    cifri.append(num%8)
    num//=8



print(cifri.count(0))