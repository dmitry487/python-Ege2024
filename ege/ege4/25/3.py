def check(num):

    deliteli = set()


    for i in range (1, int(num ** 0.5) + 1):
        if num%i == 0:
            deliteli.add(num//i)
            deliteli.add(i)


    if len(deliteli) == 5:
        return sorted(list(deliteli))
    


for num in range (123456, 987655):
    if check(num):
        print(check(num))