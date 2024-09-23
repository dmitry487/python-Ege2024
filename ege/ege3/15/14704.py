kolichestvo = 0

for a in range (200):
    flag =True

    for x in range (200):
        for y in range (200):
            if not(
                ((x < 6) <= (x ** 2 < a)) and ((y ** 2 <= a) <= (y <= 6))
            ):flag = False


    if flag:
        kolichestvo += 1


print(kolichestvo)
