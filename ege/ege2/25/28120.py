def check(num):
    
    deliteli = set()

    for i in range (1, int(num ** 0.5) + 1):
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num//i)


    if len(deliteli) == 4:
        return sorted(list(deliteli))
    return False


for num in range (201455, 201470):
    if check(num):
        print(check(num))