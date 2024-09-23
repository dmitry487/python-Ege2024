from fnmatch import fnmatch



for num in range (2024, 10 ** 10, 2024):
    if fnmatch(str(num), '3?2258*4'):
        print(num)