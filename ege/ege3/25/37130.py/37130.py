def check(num):
    delite = set()


    for i in range (2, int(num ** 0.5) + 1):
        if num%i == 0:
            if i%10 == 7 and (i != 7):
                delite.add(i)

            if (num//i)%10 == 7 and ((num//i) != 7):
                delite.add(num//i)


    return sorted(list(delite))



for num in range (600000, 600020):
    if check(num):
        print(num, check(num))