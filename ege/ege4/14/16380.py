num = 4 * 3125 ** 2019 + 3 * 625 ** 2020 - 2 * 125 ** 2021 + 25 ** 2022 - 4 * 5 ** 2023 - 2024


cifri = []


while num > 0:
    cifri.append(num%25)
    num//=25


for i in range (11, 100):
    print(cifri.count(i))