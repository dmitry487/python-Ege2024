def check(num):


    deliteli = set()

    for i in range (1, int(num ** 0.5) + 1):
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num//i)


    if len(deliteli) == 6:
        return sorted(list(deliteli)) 



for num in range (312_614, 312_651 + 1):
    if check(num):
        print(check(num)) 