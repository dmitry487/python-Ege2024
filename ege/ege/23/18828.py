def f(start, stop):
    if start == stop: return 1
    elif start > stop: return 0
    return f(start + 1, stop) + f(start + 3, stop) +\
    f(start * 3, stop)

print(f(4, 10) * f(10, 17) * f(17, 23))