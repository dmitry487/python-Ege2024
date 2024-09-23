# from string import digits, ascii_lowercase


# alph = digits + ascii_lowercase[:9]


# for x in alph:
#     res = int('98897' + x + '21', 19) + int('2' + x + '923', 19)



#     if res%18 == 0:
#         print(res//18)

print('-------------------')

num = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2024



cifri = []

while num > 0:
    cifri.append(num%25)
    num//=25


print(cifri.count(0))