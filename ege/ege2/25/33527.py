def check(num):
    deliteli = set()

    for i in range (1, int(num ** 0.5) + 1):
        if num%i == 0:
            if i%2 == 0:
                deliteli.add(i)
            if num//i%2 == 0:
                deliteli.add(num//i)
        

    if len(deliteli) == 3:
        return True
    return False


for num in range (101000000, 102_000_000 + 1):
    if check(num):
        print(num)