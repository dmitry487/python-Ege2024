from fnmatch import fnmatch

for num in range (3013, 10 ** 10 + 1, 3013):
    if fnmatch(str(num), '1?3948*5'):
        print(num)