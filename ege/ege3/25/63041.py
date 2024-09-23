from fnmatch import fnmatch

for num in range (3147, 10 ** 10, 3147):
    if fnmatch(str(num), '1*4302?1'):
        print(num)