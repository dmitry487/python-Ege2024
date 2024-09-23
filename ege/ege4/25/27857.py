def check(num):
    deliteli = set()


    for i in range (1, int(num ** 0.5) + 1):
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num%i)



    if len(deliteli) == 72:
        return sorted(list(deliteli))
    

for num in range (84052, 84131):
    if check(num):
        print(len(check(num)), num)