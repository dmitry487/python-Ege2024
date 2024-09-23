num = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625** 6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2024



cifri = []


while num > 0:
    cifri.append(num%25)
    num//=25



print(cifri.count(0))