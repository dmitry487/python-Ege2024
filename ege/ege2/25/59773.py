from fnmatch import fnmatch

for num in range(1991, 10**8 + 1, 1991):
    if fnmatch(str(num), "3?1*57"):
        print(num, num//1991)