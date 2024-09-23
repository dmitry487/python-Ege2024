def check(num):

    deliteli = set()


    for i in range (2, int(num ** 0.5) + 1):
        if num%i == 0:
            if ((i%10 == 8) and (i != 8)):
                deliteli.add(i)

            if ((num//i%10 == 8) and (num//i != 8)):
                deliteli.add(num//i)


    return sorted(list(deliteli))



for num in range(500_000, 500_100):
    if check(num):
        print(num, check(num))