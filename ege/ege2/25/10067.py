def check(num):

    deliteli = set()
    combo = [125, 216, 343, 512, 729]

    for i in range (1, int(num ** 0.5) + 1):
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num//i)

    
    if len(deliteli) in combo:
        return sorted(list(deliteli))[-2]
    return False

limit = 5
for num in range (10 ** 9, 1, -1):
    if check(num) and limit:
        print(num, check(num))
        limit -= 1