
for num in range (1, 1000):
    cifri = ''

    while num > 0:
        cifri += str(num%5)
        num//=5
        if num%25 == 0:
            num = num + num
        else:
            num += num + num%25
    r = int(num, 2)
    if r > 10000:
        print(num)
        break