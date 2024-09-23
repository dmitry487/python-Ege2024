def check(num):
    
    delite = set()


    for i in range (2, int(num ** 0.5) + 1):
        if num%i == 0:
            delite.add(i)
            delite.add(num//i)

    if len(delite) == 3:
        return sorted(list(delite))



for num in range (289_123_456, 389_123_457):
    if check(num):
        print(check(num))