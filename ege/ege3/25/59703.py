from fnmatch import fnmatch


for num in range (2023, 10 ** 8, 2023):
    if fnmatch(str(num), '3?1*57'):
        print(num, num//2023)