def f(start, stop):
    if start == stop: return 1
    elif start > stop: return 0
    return f(start + 1, stop) + f(start * 2, stop)


print(f(3, 13) * f(13, 30) * f(30, 60))