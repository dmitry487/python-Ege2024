def f(start, stop):
    if start == stop: return 1
    elif start > stop or start == 8: return 0
    return f(start + 1, stop) + f(start + 2, stop) + f(start * 2, stop)


print(f(3, 14) * f(14, 18))