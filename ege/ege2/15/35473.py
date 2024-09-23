for a in range(1, 101):
    k = 0
    for x in range(1, 1000):
        if (a % 45 == 0) and ((750 % x == 0) <= ((a % x != 0) <= (120 % x != 0))):
            k += 1
    if k == 999:
        print(a)
        break