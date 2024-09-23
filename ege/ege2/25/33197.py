def check(num):
    counter = 0

    for i in range (1, int(num**0.5) + 1):
        if num%i == 0:
            if num//i - i <= 100:
                counter += 1

    if counter > 2:
        return True
    return False

for num in range (1000000, 2000000 + 1):
    if check(num):
        print(num)

    