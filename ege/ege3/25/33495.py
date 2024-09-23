def check(num):


    deliteli = set()


    for i in range (1, int(num ** 0.5) + 1):
        if num%i == 0:
            deliteli.add(num//i - i)



    if (len(deliteli) > 2) and (sum(deliteli) <= 115): 
        return True
    return False



for num in range (2_000_000, 3_000_001):
    if check(num):
        print(num)