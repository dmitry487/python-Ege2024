# num = 4 * 3125 ** 2019 + 3 * 625 ** 2020 - 2 * 125 ** 2021 + 25 ** 2022 - 4 * 5 ** 2023 - 2024


# cifri = []


# while num > 0:
#     cifri.append(num%25)
#     num//=25


# kolichestvo = 0


# for i in range (11, 40):
#     kolichestvo += cifri.count(i)
    

# print(kolichestvo)


from string import digits, ascii_lowercase

alph = digits + ascii_lowercase[:9]



for x in alph:
    res = int('5' + x + '642535', 19) + int('78' + x + '11114', 19) + int('9334' + x + '39', 19)


    if res%18 == 0:
        print(res//18)
        