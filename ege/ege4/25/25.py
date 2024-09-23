from fnmatch import fnmatch

for num in range (98591, 10 ** 12 + 1, 98591):
    if fnmatch(str(num), '12?3*456??9'):
        print(num, num//98591)