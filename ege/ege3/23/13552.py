def f(start, stop):
    if start == stop: return 1
    elif start > stop: return 0
    return f(start + 1, stop) + f(start + 2, stop) + f(start + 4, stop)

print(f(1, 8) * f(8, 15))