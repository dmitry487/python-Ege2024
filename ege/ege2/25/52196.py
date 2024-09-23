from fnmatch import fnmatch


for num in range (3127, 10 ** 9 + 1, 3127):
    if fnmatch(str(num), "12*93?1?"):
        print(num)