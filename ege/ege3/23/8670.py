def f(start, stop):
    if start == stop: return 1
    elif start > stop: return 0
    return f(start + 3, stop) + f(start + 4, stop) +\
    f(start + 5, stop)


print(f(22, 42))