from fnmatch import fnmatch

for num in range (98591, 10 ** 10 + 1, 98591):
    if fnmatch(str(num), '5?2*3?3?'):
        print(num, num//98591)