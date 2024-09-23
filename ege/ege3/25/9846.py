from fnmatch import fnmatch



for num in range (2025, 10 **8 + 1, 2025):
    if fnmatch(str(num), "12*34?5"):
        print(num, num//2025)