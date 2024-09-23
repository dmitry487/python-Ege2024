from fnmatch import fnmatch

def check(num):
    deliteli = set()

    for i in range (1, int(num ** 0.5) + 1):
        if num%i == 0:
            if num//i == num:
                deliteli.add(i)
                deliteli.add(num//i)
            
    return sorted(list(deliteli))
            
def netr(num):
    deliteli = set()
    
    for i in range (2, int(num ** 0.5) + 1):
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num//i)

    return sorted(list(deliteli))
        

for num in range (1, 10 ** 8):
    if fnmatch(str(num), "13*7?5") and (sum(check(num))%2024 == 0):
        print(num, (netr(num)[-1]))