from fnmatch import fnmatch


for num in range(23, 10**9 + 1, 23):
    if fnmatch(str(num), "12345?7?8"):
        print(num, num//23)