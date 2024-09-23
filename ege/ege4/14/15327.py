num = 3 * 2187 ** 2020 + 3 * 729 ** 2021 - 2 * 81 ** 2022 + 27 ** 2023 - 4 * 3 ** 2024 - 2029

cifri = []



while num > 0:
    cifri.append(num%27)
    num//=27


print(cifri.count(5))
print(cifri.count(0))
print(len(cifri))
print(4714 - 1344)