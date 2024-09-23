def check(num):
    deliteli = []

    for i in range (1, int(num ** 0.5) + 1):
        if num%i == 0 and num%10 != 7:
            if ((i%10 == 7) or (num//i%10 == 7)) and\
                  (i != 7 and num//i%i != 7):
                if i%10 == 7:
                    deliteli.append(i)
                if num//i%10 == 7:
                    deliteli.append(num//i)

    deliteli = sorted(deliteli)
    if deliteli:
        return deliteli[0]
limit = 5
for num in range (600_000, 700000):
    if check(num) and limit:

        print(num, check(num))
        limit -= 1
