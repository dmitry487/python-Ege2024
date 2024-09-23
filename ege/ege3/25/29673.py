def check(num):

    deliteli = set()

    for i in range (2, int(num ** 0.5) + 1):
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num//i)

    if len(deliteli) == 3:
        return sorted(list(deliteli[-1]))
    

for num in range (123456789, 223456789 + 1):
    if check(num):
        print(check(num))