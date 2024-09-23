def check(num):

    deliteli = set()


    for i in range (2, int(num ** 0.5) + 1):
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num//i)

    if len(deliteli) >= 5:
        return sorted(list(deliteli), reverse = True)[4]
    

for num in range (300_000_000, 300_000_010):
    if check(num):
        print(check(num))