from fnmatch import fnmatch


for num in range(3147, 10**10 + 1, 3147):
    if fnmatch(str(num), "1*4239?7"):
        print(num)