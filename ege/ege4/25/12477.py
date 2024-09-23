from fnmatch import *

def check(num):
    deliteli = set()
    for i in range (1, int(num ** 0.5) + 1):
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num//i)

    if len(deliteli) == 2:
        return True
    return False


for num in range (1, 10**7, 1):
    if fnmatch(str(num), '3?1111*') and check(num):
        print(num)