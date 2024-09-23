num = 4 * 3125 ** 2019 + 3 * 625 ** 2020 - 2 * 125 ** 2021 + 25 ** 2022 - 4 * 5 ** 2023 - 2024


cifri = []


while num > 0:
    cifri.append(num%25)
    num//=25


print(set(cifri))
print(cifri.count(15) + cifri.count(19) + cifri.count(20) + cifri.count(21) + cifri.count(24))
