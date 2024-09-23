def check(num):

    deliteli = set()

    for i in range(1, int(num ** 0.5) + 1):
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num//i)

    return len(deliteli)


res = []


for num in range (120115, 120200 + 1):
    res.append([check(num), num])
    print(sorted(res))