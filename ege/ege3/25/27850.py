def check(num):
    deliteli = set()

    for i in range (1, int(num ** 0.5) + 1):
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num//i)


    return sorted(list(deliteli))


for nums in range (245_690, 245_756 + 1):
    if check(nums):
        print(nums)