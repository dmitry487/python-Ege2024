from fnmatch import fnmatch



for num in range (42, 2 * 10 ** 8 + 1, 42):
    if fnmatch(str(num), '?2*4*0') and not(fnmatch(str(num), '1*7*')):
        print(num, num//42)