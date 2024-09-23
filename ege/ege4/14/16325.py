num = 2 * 729 ** 2014 + 2 * 243 ** 2016 - 2 * 81 ** 2018 + 2 * 27 ** 2020 - 2 * 9 ** 2022 - 2024


cifri = []


while num > 0:
    cifri.append(num%27)
    num//=27


for i in range (10, 100):
    if cifri.count(i) > 0:
        print(cifri.count(i))


#2687
        