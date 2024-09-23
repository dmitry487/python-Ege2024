def check(num):
    deliteli = []

    for i in range (2, int(num ** 0.5) + 1):
        if num%i == 0 and (i!= num or num//i != num):
            if (num//i%10 == 8 or i%10 == 8) and\
            (num//i != 8 and i != 8):
                if num//i%10 == 8:
                    deliteli.append(num//i)
                if i%10 == 8:
                    deliteli.append(i)

    deliteli = sorted(deliteli)
    if deliteli:
        return deliteli[0]

limit = 5
for num in range (500000, 1000000):
    if check(num) and limit:
        print(num, check(num))
        limit -= 1
                
                


     