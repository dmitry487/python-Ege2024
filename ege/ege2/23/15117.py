def f(start, stop):
    if start == stop: return 1
    elif start > stop or start == 15: return 0
    return f(start + 1, stop) + f(start + 2, stop)


print(f(3, 9) * f(9, 20))