def check(num):

    deliteli = set()


    for i in range (2, int(num ** 0.5) + 1):
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num//i)


    return sorted(list(deliteli))
step = 5
while step > 0:

    for num in range (10_000_00, 10_050_00 + 1):
        if check(num):
            print(check(num), num)
            step -=1
