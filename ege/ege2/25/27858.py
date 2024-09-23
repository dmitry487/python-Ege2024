def check(num):

    deliteli = set()

    for i in range (1, int(num ** 0.5) + 1):
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num//i)

    return sorted(list(deliteli))


len_max = 0


for num in range (120115, 120200 + 1):
    len_max = max(len_max, len(check(num)))

    if len_max == len(check(num)):
        print(num, len_max)