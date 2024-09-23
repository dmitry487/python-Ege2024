from itertools import combinations

f = open('ege3/27/1/1.txt')

nums = [[int(i) for i in nums.split()] for nums in f]




spis_obsh = combinations(
    sorted([nums]), 2
)
print(list(spis_obsh))
# kolichestvo = 0
# for umnoj1, umnoj2 in spis_obsh:
#     flag = True

#     if not(umnoj1 * umnoj2)%62 == 0:
#         flag = False

#     if flag:
#         kolichestvo += 1


# print(kolichestvo)

    
# print('-------------------------')


# from itertools import combinations

# n = open('ege3/27/1/11.txt')


# nums1 = [int(i) for i in n]

# spis_obsh1 = combinations(
#     sorted([nums1]), 2
# )

# print(list(spis_obsh1))
# counter = 0
# for umnoj1, umnoj2 in spis_obsh1:
#     flag = True

#     if not(umnoj1 * umnoj2)%62 == 0:
#         flag = False

#     if flag:
#         counter += 1


# print(counter)