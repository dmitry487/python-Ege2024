def check(num):


    deliteli = set()


    for i in range (1, int(num ** 0.5) + 1):
        maxmin = []
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num//i)
    deliteli = sorted(list(deliteli))
    if len(deliteli) != 0:
        maxmin.append(deliteli[-1] + deliteli[0])
    if maxmin%7 == 3:
        return True
    return False
    

for num in range (452_021, 500001):
    if check(num):
        print(num)