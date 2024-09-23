def check(num):


    deliteli = set()


    for i in range (2, int(num ** 0.5) + 1):
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num//i)

    
    if len(deliteli) == 2:
        return sorted(list(deliteli))
    

for num in range (17_44_57, 17_45_05 + 1):
    if check(num):
        print(check(num))

